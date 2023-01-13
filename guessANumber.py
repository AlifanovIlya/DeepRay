from random import randint

startNumber = randint(1, 100)
endNumber = randint(110, 10000)

computerNumber = randint(startNumber, endNumber)

def gamerNumber():
	number = input(f'''Твой противник загадал число между {startNumber} и {endNumber}.
Тебе нужно его угадать.\n\n''')
	if number.isdigit() != True:
		while number.isdigit() != True:
			print('\nТы вписал что-то не то.\n')
			number = input(f'''Твой противник загадал число между {startNumber} и {endNumber}.
Тебе нужно его угадать.\n\n''')
	return int(number)

def game():
	number = 0
	while number != computerNumber:
		number = gamerNumber()
		if number < startNumber or number > endNumber:
			print('\nТы выходишь за рамки, так нельзя.\n')
		elif number < computerNumber:
			print('\nПопробуй число побольше\n')
		elif number > computerNumber:
			print('\nПопробуй число поменьше\n')
	print(f'\nМолодец, ты угадал! Это было чило {computerNumber}')
