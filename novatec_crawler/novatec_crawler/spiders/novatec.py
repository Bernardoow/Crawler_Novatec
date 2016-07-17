# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.loader import ItemLoader
from novatec_crawler.items import NovatecLivroItem
class NovatecSpider(scrapy.Spider):
    name = "novatec"
    allowed_domains = ["novatec.com.br"]
    start_urls = [
        'http://www.novatec.com.br/',
    ]

    rules = (Rule(SgmlLinkExtractor(), callback='parse', follow=False),)
    def parse(self, response):

        for x in response.xpath('//a[contains(@href, "lista.php")]/@href').extract():
            url = "http://www.novatec.com.br/"+x.replace('../','')
            yield scrapy.Request(url=url, callback=self.parse_item)


    def parse_item(self, response):

        items = response.xpath('//td[contains(@valign, "top")]')
        for item in items:
            nome = item.xpath('.//a[contains(@href, "livros/")]').extract()
            autor = item.xpath('.//a[contains(@href, "autores/")]').extract()
            if nome and autor:
                import unicodedata
                livro = item.xpath('.//a[contains(@href, "livros/")]//text()').extract_first()
                autores = item.xpath('.//a[contains(@href, "autores/")]//text()').extract()
                separacao = " "
                livro = NovatecLivroItem(nome = unicodedata.normalize(
                    'NFKD', livro).encode('ascii','ignore'), autor = unicodedata.normalize('NFKD', separacao.join(autores)).encode('ascii','ignore'))
                yield livro


        next_page = response.xpath(
            '//a[contains(.,"xima >>")]/@href'
        ).extract_first()
        if next_page:
            yield scrapy.Request(url='http://www.novatec.com.br/'+next_page, callback=self.parse_item)





