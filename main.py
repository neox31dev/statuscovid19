import json
import requests
import time
import os
from getpass import *

vermelho = '\033[1;31m'
verde = '\033[1;32m'
reset = '\033[0;0m'
bullet = '\u2022 '

def cls():
	if os.name == "nt":
		os.system('cls')
	else:
		os.system('clear')
ascii_art = '''
   ___           _     _       _  ___  
  / __\_____   _(_) __| |     / |/ _ \ 
 / /  / _ \ \ / / |/ _` |_____| | (_) |
/ /__| (_) \ V /| | (_| |_____| |\__, |
\____/\___/ \_/ |_|\__,_|     |_|  /_/ 
                                       
'''

def code():
	cls()
	print(ascii_art)
	pais = input('Escreva aqui o seu pais (PT, US, ES): ')
	if pais == '':
		main()
	else:
		pass
	url = requests.get('https://covid19-api.org/api/status/'+pais).json()
	print('\n'+bullet+'País: '+verde+url['country']+reset)
	print(bullet+'Ultima Atualização: '+verde+url['last_update']+reset)
	print(bullet+'Recuperados: '+verde+str(url['recovered'])+reset)
	print(bullet+'Casos: '+vermelho+str(url['cases'])+reset)
	print(bullet+'Mortes: '+vermelho+str(url['deaths'])+reset)
	input('\n/> Clica no Enter para começar denovo')
	code()
code()