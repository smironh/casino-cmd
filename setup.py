
#1.0

from os import system
from colorama import init, Fore, Back, Style
from termcolor import colored

import sys
import time
import random

init()

system('cls')
print(colored('''
  ___    __ _   ___  (_)  _ __     ___
 / __|  / _` | / __| | | | '_ \   / _ \ 
| (__  | (_| | \__ \ | | | | | | | (_) |
 \___|  \__,_| |___/ |_| |_| |_|  \___/
'''))


#  ___    __ _   ___  (_)  _ __     ___
# / __|  / _` | / __| | | | '_ \   / _ \ 
#| (__  | (_| | \__ \ | | | | | | | (_) |
# \___|  \__,_| |___/ |_| |_| |_|  \___/

def casino():
	m = 1000
	win = ['''  
  _     _     _ 
 | |   | |   | |
 | |   | |   | |
 |_|   |_|   |_|
 (_)   (_)   (_)
                
	''',
	 '''
                
                
                
  _     _     _ 
 (_)   (_)   (_)
                
	 ''',
	 '''
  _     _     _ 
 | |   | |   | |
 | |   | |   | |
 | |   | |   | |
 | |   | |   | |
 |_|   |_|   |_|

	 ''']
	nowin =[
		"""
  _     _       
 | |   | |      
 | |   | |      
 |_|   |_|    _ 
 (_)   (_)   (_)
                
		""",
		"""
  _     _     _ 
 | |   | |   | |
 | |   | |   | |
 |_|   |_|   | |
 (_)   (_)   | |
             |_|

		""",
		"""
              _ 
             | |
             | |
  _     _    |_|
 (_)   (_)   (_)
		""",
		"""
              _ 
             | |
             | |
  _     _    | |
 (_)   (_)   | |
             |_|
		""",
		"""
  _     _       
 | |   | |      
 | |   | |      
 | |   | |    _ 
 | |   | |   (_)
 |_|   |_|      

		""",
		"""
  _     _     _ 
 | |   | |   | |
 | |   | |   | |
 | |   | |   |_|
 | |   | |   (_)
 |_|   |_|      

		""",
		"""
        _     _ 
       | |   | |
       | |   | |
  _    |_|   |_|
 (_)   (_)   (_)
                
		""",
		"""
  _     _     _ 
 | |   | |   | |
 | |   | |   | |
 | |   |_|   |_|
 | |   (_)   (_)
 |_|            

		""",
		"""
  _     _     _ 
 | |   | |   | |
 | |   | |   | |
 |_|   | |   | |
 (_)   | |   | |
       |_|   |_|

		""",
		"""
  _     _     _ 
 | |   | |   | |
 | |   | |   | |
 |_|   | |   |_|
 (_)   | |   (_)
       |_|      
		""",
		"""	
  _             
 | |            
 | |            
 |_|    _     _ 
 (_)   (_)   (_)
                
		""",
		"""
  _             
 | |            
 | |            
 | |    _     _ 
 | |   (_)   (_)
 |_|            

		"""
			]
	fail = [
		"""
        _     _ 
       | |   | |
       | |   | |
  _    |_|   | |
 (_)   (_)   | |
             |_|

		""",
		"""
        _     _ 
       | |   | |
       | |   | |
  _    | |   |_|
 (_)   | |   (_)
       |_|      
		""",
		"""
  _     _       
 | |   | |      
 | |   | |      
 | |   |_|    _ 
 | |   (_)   (_)
 |_|            

		""",
		"""
  _     _       
 | |   | |      
 | |   | |      
 |_|   | |    _ 
 (_)   | |   (_)
       |_|      

		"""]
	while True:
		if m == 0:
			print('''
У вас нет денег и у вас есть 3 выбора
1 - Пойти попрошайнечить(Быстро но можно собрать всего 10 рублей)

2 - Своровать(Опасно но можно украсть 1к)

3 - Пойти работать(Долго но зп 500 рублей)
''')
			main = input('>')
			if main == '1':
				while m < 11:
					time.sleep(1)
					zp = random.randint(1, 3)
					m += zp
					print(f'{zp} баланс - {m} рубля')
				system('cls')
				continue
			if main == '2':
				sudb = random.randint(1 , 2)
				clever = input('Зажать клевер в руке? (y)')
				if clever == 'y':
					m += 1000
					system('cls')
					continue
				else:
					if sudb == 1:
						system('cls')
						print('Вы украли касарь у бабушки на улице!')
						m += 1000
						continue
					if sudb == 2:
						print('GAME OVER вы в тюрьме на пожизненом. В следущий раз повезет!')
						input('Нажмите Enter')
						exit()
			if main == '3':
				while m < 500:
					time.sleep(1)
					m += 50
					print(f'Час отработан + 50 рублей | Балланс - {m}')
				system('cls')
				continue
			else:
				continue
				system('cls')
				print('Выберите что то')
		print(f'''Рублей на балансе - {m}''')
		stav = input('Ставка >')
		try:
			if stav == 'exit':
				exit()
			if stav == 'givemoneypls':
				system('cls')
				m += 1000
				continue
			if stav == 'suicide':
				system('cls')
				m = 0
				continue
			val = int(stav)
		except ValueError:
			system('cls')
			print("Нужно вводить число!")
			continue
		if val > m:
			system('cls')
			print('Эмммм у тебя денег не хватит')
			continue
		elif val < 0:
			system('cls')
			print('Чего?')
			continue
		yeah = input("Крутить - (y)(Если ошблись ставкой нажмите Enter) >")
		system('cls')
		if yeah == 'y':
			a = random.randint(1 , 3)
			if a == 1:
				b = random.choice(win)
				m += val
				system('cls')
				print(b)
				print(f'Вы выйграли {val}')
			elif a == 2:
				b = random.choice(nowin)
				system('cls')
				print(b)
				print(f'Вы ничего не выйграли :(')
			elif a == 3:
				b = random.choice(fail)
				m -= val
				system('cls')
				print(b)
				print(f'Вы проиграли {val} :(')
			else:continue

def info():
	print('''
Читы:
givemoney - деньги
suicide - выбросить все деньги
exit - выход
''')

def start():		
	while True:
		a = input('Играть (y)\nИнформация (n)\n>')
		if a == 'y':
			system('cls')
			casino()
		if a == 'n':
			system('cls')
			info()
		else:
			print('вы отказались от игры(')
			break

start()
