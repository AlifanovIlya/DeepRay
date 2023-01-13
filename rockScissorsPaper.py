from random import randint

def game():
	computerChoose = randint(1, 3)
	result = 0

	while result != 1:
		gamerChoose = input('''Что бы пройти дальше,тебе нужно победить в игре "Камень, ножницы, бумага".\n
Впиши то, что ты хочешь выбрать.\n\n''')
		if gamerChoose.lower() == 'камень':
			if computerChoose == 1:
				print('\nУ соперника тоже выпал Камень, нужно сыграть снова.')
				result = 0
			elif computerChoose == 2:
				print('\nУ соперника выпали Ножницы, ты победил!')
				result = 1
			elif computerChoose == 3:
				print('\nУ соперника выпала Бумага, ты проиграл. Очень жаль.')
				result = 0
		elif gamerChoose.lower() == 'ножницы':
			if computerChoose == 1:
				print('\nУ соперника выпал Камень, ты проиграл. Очень жаль')
				result = 0
			elif computerChoose == 2:
				print('\nУ соперника тоже выпали Ножницы, нужно сыграть снова')
				result = 0
			elif computerChoose == 3:
				print('\nУ соперника выпала Бумага, ты победил!')
				result = 1
		elif gamerChoose.lower() == 'бумага':
			if computerChoose == 1:
				print('\nУ соперника выпал Камень, ты победил!')
				result = 1
			elif computerChoose == 2:
				print('\nУ соперника выпали Ножницы, ты проиграл. Очень жаль')
				result = 0
			elif computerChoose == 3:
				print('\nУ соперника тоже выпала Бумага, нужно сыграть снова.')
				result = 0
		else:
			print('\nТы вписал что-то не то. Впиши, то, что ты хочешь выбрать.')
