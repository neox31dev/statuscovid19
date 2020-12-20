import requests
import time
import os

vermelho = '\033[1;31m'
verde = '\033[1;32m'
reset = '\033[0;0m'
bullet = '\u2022 '

def cls():
	if os.name == "nt":
		os.system('cls')
	else:
		os.system('clear')

ascii_art = '''   ___           _     _       _  ___  
  / __\_____   _(_) __| |     / |/ _ \ 
 / /  / _ \ \ / / |/ _` |_____| | (_) |
/ /__| (_) \ V /| | (_| |_____| |\__, |
\____/\___/ \_/ |_|\__,_|     |_|  /_/ 
              coded by neox                  
'''

def code():
	cls()
	print(ascii_art)
	pais = input('Escreva aqui o seu pais (PT, US, ES): ')
	if pais == '':
		print('Escreva alguma coisa.')
		time.sleep(1.5)
		code()
	else:
		pass
	try:
		#Fazer request api
		url = requests.get('https://covid19-api.org/api/status/'+pais).json()
		
		#Mostrar Todos os Resultados
		print('\n'+bullet+'País: '+verde+url['country']+reset)
		print(bullet+'Ultima Atualização: '+verde+url['last_update']+reset)
		print(bullet+'Recuperados: '+verde+str(url['recovered'])+reset)
		print(bullet+'Casos: '+vermelho+str(url['cases'])+reset)
		print(bullet+'Mortes: '+vermelho+str(url['deaths'])+reset)
		
		#Começar denovo
		começar_denovo = input('\nQueres começar denovo? s/n ')
		if começar_denovo == 's':
			code()
		else:
			quit()

	except KeyError:
		print('Pais não encontrado.')
		time.sleep(1.5)
		code()
code()
