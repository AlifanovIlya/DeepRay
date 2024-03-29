import characters, rockScissorsPaper, guessANumber

def nextMessage():
	input_key = input('\n***Что бы увидеть следующее сообщение, нажми клавишу "Enter"***\n')

	while input_key != '':
		input_key = input('''\n*** Это какая-то другая клавиша! ***
\n*** Что бы увидеть следующее сообщение, нажми клавишу "Enter" ***\n''')


def main():

	print('\nВыбери героя, за которого хочешь играть. Но сначала посмотри на всех.')

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

	print('\nОтлично, а теперь начнем.')

	nextMessage()

	print('''Вы устало опускаетесь в офисное кресло: еще один долгий
день, полный деловых встреч, остался позади. В данный
момент вы расследуете исчезновения, которые уже две
недели происходят в богатом районе, но результатов все еще
нет.''')

	nextMessage()

	print('''Раздается телефонный звонок. Вы поднимаете трубку и
слышите испуганный голос пожилого мужчины:''')

	nextMessage()

	print('''-- Э-это вы тот сыщик, который посещал поместье
Вандербильтов?''')

	nextMessage()

	print('''Вы просматриваете документы на столе. Уильям
Вандербильт: богатый холостяк, мать недавно скончалась. Он
отказался встретиться с вами, но вы смогли побеседовать с
несколькими людьми из прислуги.''')

	nextMessage()

	print('''-- Это Юджин, дворецкий мистера Вандербильта. Я-я не
знал, к кому еще обратиться. Полиция думает, что я
свихнулся. Здесь происходит что-то противоестественное. Я
беспокоюсь за хозяина, мне кажется он в опасности.
Пожалуйста помогите нам!''')

	nextMessage()

	print('''Наконец-то наводка! Вы вешаете трубку, накидываете пальто
и отправляетесь в поместье Вандербильтов.''')
	


if __name__ == '__main__':
	main()
