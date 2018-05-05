#!/usr/bin/env python

import requests
import json
import math

def consulta(titulo, page):
    try:
        req = requests.get("http://www.omdbapi.com/?s="+titulo+"&page="+page+"&apikey=<key>")
        dictionaire = json.loads(req.text)
        return dictionaire
    except Exception as erro:
        print("Erro->",erro)
        return False


def print_detalhes(items, op):

    print('-----Resultado da consulta------')
    qtdPage = int(items['totalResults']) / 10

    for x in range(math.ceil(qtdPage)):
        x = x+1
        print('Pagina: ',x)
        r = consulta(op, str(x))

        for item in r['Search']:
            print('Título:',item['Title'], '- Ano:',item['Year'], '- Tipo:',item['Type'])

    print('\nResultados encontrados:', items['totalResults'])
    print('-----Consulta finalizada--------')


sair = False
while not sair:
    op = input("Digite o nome do filme ou aperte '1' para sair:\n")

    if op == '1':
        sair = True
        print('Saindo...')
    else:
        results = consulta(op, '1')
        if results["Response"] == 'False':
            print("Not found")
        else:
            print_detalhes(results, op)
