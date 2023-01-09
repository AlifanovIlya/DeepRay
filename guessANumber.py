from random import randint

def game():
	startNumber = randint(1, 100)
	endNumber = randint(110, 10000)

	computerNumber = randint(startNumber, endNumber)

	gamerNumber = input(f'''Твой противник загадалчисло от {startNumber} до {endNumber}.\n
Тебе нужно его угадать.\n''')

	while gamerNumber != computerNumber:
		if gamerNumber < startNumber or gamerNumber > endNumber:
			print('Так нельзя, ты выходишь за рамки!')
		elif gamerNumber > computerNumber:
			print('Попробуй число поменьше.')
		elif gamerNumber < computerNumber:
			print('попробуй число побольше.')

	print(f'Молодец! Было загалано число {computerNumber}')