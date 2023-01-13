import characters, rockScissorsPaper, guessANumber

def nextMessage():
	input_key = input('\n***Что бы увидеть следующее сообщение, нажми клавишу "Enter"***\n')

	while input_key != '':
		input_key = input('''\n*** Это какая-то другая клавиша! ***
\n*** Что бы увидеть следующее сообщение, нажми клавишу "Enter" ***\n''')


def main():
	print('''\nНу, здравствуй!
Добро пожаловать в дом ужасов Ха-Ха!
Ты - сыщик, и тебе надо, кто бы мог подумать, найти!
А вот, что найти, это ты и узнаешь!''')

	nextMessage()

	print('Выбери героя, за которого хочешь играть. Но сначала посмотри на всех.')

	nextMessage()

	characters.lookAtCharacters()

	nextMessage()

	mainCharacterName = input('Впиши полное имя персонажа, которого хочешь выбрать\n\n')
	characterNamesArray = ['рита янг',
	'карсон синклер',
	'агата крейн',
	'венди адамс',
	'престон фэрмонт',
	'минь тхи фанг',
	'уильям йорик',
	'отец матео']

	while mainCharacterName.lower() not in characterNamesArray:
		mainCharacterName = input('\nЭто не правильное имя, впиши полное имя персонажа, которого хочешь выбрать\n\n')

	print('\nОтлично, а теперь продолжим.')

	nextMessage()

	print('Перед тобой дверь, ее нужно взломать')

	rockScissorsPaper.game()

	nextMessage()

	print('Ого,еще одна дверь, ну-ка, взломай и ее.\n')

	guessANumber.game()


	


if __name__ == '__main__':
	main()
