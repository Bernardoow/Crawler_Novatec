#-*- coding: utf-8 -*-
#__author__ = Bernardo Gomes
#16/07/2016 
#09:28
import json
from pprint import pprint

class Livro(object):
    """docstring for ClassName"""

    def __init__(self, nome, autor):
        super(Livro, self).__init__()
        self.nome, self.autor = nome, autor


    def __eq__(self, other):
        return (isinstance(other, self.__class__)
                and self.nome == other.nome
                and self.autor == other.autor
                )


    def __ne__(self, other):
        return not self.__eq__(other)


    def __str__(self):
        return '{} - {} '.format(self.nome, self.autor)


    def __repr__(self):
        return '{} - {} '.format(self.nome, self.autor)

if __name__ == '__main__':

    listaAntiga = []
    listaNova = []
    with open('saida_antiga.json') as data_file:
        data = json.load(data_file)

    with open('saida_nova.json') as data_file:
        data_nova = json.load(data_file)


    [listaAntiga.append(Livro(nome = x['nome'], autor = x['autor']))
         for x in data]

    [listaNova.append(Livro(nome=x['nome'], autor=x['autor']))
     for x in data_nova]

    listaDeNovoItens = [x for x in listaNova if not (x in listaAntiga)]
    listaDeItensQueSairam = [x for x in listaAntiga if not (x in listaNova)]

    print(listaDeNovoItens)
    print(listaDeItensQueSairam)
