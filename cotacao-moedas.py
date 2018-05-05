#!/usr/bin/env python

import requests
import json
import datetime

# utilizando o menu
def utilizando_menu(opcao):
        if opcao == 1:
                result = consult('USD')
                show_result(result['valores']['USD']['nome'],result['valores']['USD']['ultima_consulta'],result['valores']['USD']['valor'],result['valores']['USD']['fonte'])
        elif opcao == 2:
                result = consult('EUR')
                show_result(result['valores']['EUR']['nome'],result['valores']['EUR']['ultima_consulta'],result['valores']['EUR']['valor'],result['valores']['EUR']['fonte'])
        elif opcao == 3:
                result = consult('BTC')
                show_result(result['valores']['BTC']['nome'],result['valores']['BTC']['ultima_consulta'],result['valores']['BTC']['valor'],result['valores']['BTC']['fonte'])
        elif opcao == 9:
                print('Bye Bye...')
        else:
                menu()

# exibir menu
def menu():
	print('\n-----------MENU------------')
	print('1. Dolar-------------------')
	print('2. Euro--------------------')
	print('3. Bitcoin-----------------')
	print('9. Exit--------------------')
		
	opcao = float(raw_input('\nSelecione uma moeda e veja sua cotacao: '))
	utilizando_menu(opcao)

# realizando a consulta
def consult(coin):
	try:
		req = requests.get('http://api.promasters.net.br/cotacao/v1/valores?moedas='+coin+'&alt=json')
		return json.loads(req.text)
	except Exception as e:
		print('Error', e)
		return false

# exibindo o resultado
def show_result(moeda,ultima_consulta,valor,fonte):
	print '\n------------Busca realizada----------------------------'
	print 'Moeda: ',moeda
	print 'Ultima consulta: ', datetime.datetime.fromtimestamp(int(ultima_consulta)).strftime('%H-%M-%S %d:%m:%Y')
	print 'Cotacao de hoje: ',valor
	print 'Fonte: ',fonte
	print '-------------------------------------------------------'	
	menu()

menu()
