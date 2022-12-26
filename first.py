import characters

def nextMessage():
	input_key = input('\n***Что бы увидеть следующее сообщение, нажми клавишу "Enter"***\n')

	while input_key != '':
		print('\n*** Это какая-то другая клавиша! ***\n')
		input_key = input('\n*** Что бы увидеть следующее сообщение, нажми клавишу "Enter" ***\n')


def main():
	print('''Ну, здравствуй!
Добро пожаловать в дом ужасов Ха-Ха!
Ты - сыщик, и тебе надо, кто бы мог подумать, найти!
А вот, что найти, это ты и узнаешь!''')

	nextMessage()

	print('Выбери героя, за которого хочешь играть. Но сначала посмотри на всех.')

	nextMessage()

	characters.lookAtCharacters()

	nextMessage()

	mainCharacterName = input('Впиши полное имя персонажа, которого хочешь выбрать\n\n')
	characterNamesArray = ['Рита Янг',
	'Карсон Синклер',
	'Агата Крейн',
	'Венди Адамс',
	'Престон Фэрмонт',
	'Минь Тхи Фанг',
	'Уильям Йорик',
	'Отец Матео']
	while mainCharacterName not in characterNamesArray:
		mainCharacterName = input('Это не правильное имя, впиши полное имя персонажа, которого хочешь выбрать\n\n')

	print('\nОтлично, а теперь продолжим.\n')

	print(characters.charactersSpecials(mainCharacterName, 'health'))


if __name__ == '__main__':
	main()
