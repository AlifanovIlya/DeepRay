from random import randint

def game():
	computerChoose = randint(1, 3)

	gamerChoose = input('''Что бы пройти дальше,тебе нужно победить в игре "Камень, ножницы, бумага".\n
Впиши то, что ты хочешь выбрать.\n\n''')

	if gamerChoose == 'камень':
		if computerChoose == 1:
			print('\nУ соперника тоже выпал Камень, нужно сыграть снова.')
			return False
		elif computerChoose == 2:
			print('\nУ соперника выпали Ножницы, ты победил!')
			return True
		elif computerChoose == 3:
			print('\nУ соперника выпала Бумага, ты проиграл. Очень жаль.')
			return False
	elif gamerChoose == 'ножницы':
		if computerChoose == 1:
			print('\nУ соперника выпал Камень, ты проиграл. Очень жаль')
			return False
		elif computerChoose == 2:
			print('\nУ соперника тоже выпали Ножницы, нужно сыграть снова')
			return False
		elif computerChoose == 3:
			print('\nУ соперника выпала Бумага, ты победил!')
			return True
	elif gamerChoose == 'бумага':
		if computerChoose == 1:
			print('\nУ соперника выпал Камень, ты победил!')
			return True
		elif computerChoose == 2:
			print('\nУ соперника выпали Ножницы, ты проиграл. Очень жаль')
			return False
		elif computerChoose == 3:
			print('\nУ соперника тоже выпала Бумага, нужно сыграть снова.')
			return False
	else:
		print('\nТы вписал что-то не то. Впиши, то, что ты хочешь выбрать.')
