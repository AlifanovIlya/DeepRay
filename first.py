def nextMessage():
	input_key = input('\n***Что бы увидеть следующее сообщение, нажми клавишу "Enter"***\n')

	while input_key != '':
		print('\n*** Это какая-то другая клавиша! ***\n')
		input_key = input('\n*** Что бы увидеть следующее сообщение, нажми клавишу "Enter" ***\n')

def choseCharacter():
	def characterRita():
		name = 'Рита Янг'
		role = 'Спортсменка'
		health = 9
		force = 5
		agility = 4
		attention = 3
		knowledge = 3
		communication = 2
		will = 4
		print(f'Рита Янг\n Спортсменка\n Здоровье = {health}\n Сила = {force}\n Ловкость = {agility}\n Внимание = {attention}\n Знания = {knowledge}\n Общение = {communication}\n Воля = {will}')

	def characterKarson():
		name = 'Карсон Синклер'
		role = 'Дворецкий'
		health = 8
		force = 3
		agility = 2
		attention = 5
		knowledge = 4
		communication = 4
		will = 3
		print(f'Карсон Синклер\n Дворецкий\n Здоровье = {health}\n Сила = {force}\n Ловкость = {agility}\n Внимание = {attention}\n Знания = {knowledge}\n Общение = {communication}\n Воля = {will}')

	def characterAgata():
		name = 'Агата Крейн'
		role = 'Парапсихолог'
		health = 5
		force = 2
		agility = 3
		attention = 4
		knowledge = 5
		communication = 3
		will = 4
		print(f'Агата Крейн\n Парапсихолог\n Здоровье = {health}\n Сила = {force}\n Ловкость = {agility}\n Внимание = {attention}\n Знания = {knowledge}\n Общение = {communication}\n Воля = {will}')

	def characterVendi():
		name = 'Венди Адамс'
		role = 'Беспризорница'
		health = 6
		force = 3
		agility = 5
		attention = 4
		knowledge = 3
		communication = 3
		will = 3
		print(f'Венди Адамс\n Беспризорница\n Здоровье = {health}\n Сила = {force}\n Ловкость = {agility}\n Внимание = {attention}\n Знания = {knowledge}\n Общение = {communication}\n Воля = {will}')

	def characterPreston():
		name = 'Престон Фэрмонт'
		role = 'Миллионер'
		health = 8
		force = 4
		agility = 4
		attention = 3
		knowledge = 2
		communication = 5
		will = 3
		print(f'Пестон Фэрмонт\n Миллионер\n Здоровье = {health}\n Сила = {force}\n Ловкость = {agility}\n Внимание = {attention}\n Знания = {knowledge}\n Общение = {communication}\n Воля = {will}')

	def characterMin():
		name = 'Минь Тхи Фанг'
		role = 'Серкетарша'
		health = 7
		force = 3
		agility = 4
		attention = 4
		knowledge = 3
		communication = 4
		will = 3
		print(f'Минь Тхи Фанг\n Серкетарша\n Здоровье = {health}\n Сила = {force}\n Ловкость = {agility}\n Внимание = {attention}\n Знания = {knowledge}\n Общение = {communication}\n Воля = {will}')

	def characterUilyam():
		name = 'Уильям Йорик'
		role = 'Могильщик'
		health = 7
		force = 4
		agility = 3
		attention = 4
		knowledge = 3
		communication = 3
		will = 4
		print(f'Уильям Йорик\n Могильщик\n Здоровье = {health}\n Сила = {force}\n Ловкость = {agility}\n Внимание = {attention}\n Знания = {knowledge}\n Общение = {communication}\n Воля = {will}')

	def characterMateo():
		name = 'Отец Матео'
		role = 'Священник'
		health = 6
		force = 3
		agility = 3
		attention = 2
		knowledge = 4
		communication = 4
		will = 5
		print(f'Отец Матео\n Священник\n Здоровье = {health}\n Сила = {force}\n Ловкость = {agility}\n Внимание = {attention}\n Знания = {knowledge}\n Общение = {communication}\n Воля = {will}')

	characterRita()

	nextMessage()

	characterKarson()

	nextMessage()

	characterAgata()

	nextMessage()

	characterVendi()

	nextMessage()

	characterPreston()

	nextMessage()

	characterMin()

	nextMessage()

	characterUilyam()

	nextMessage()

	characterMateo()






def main():
	print('Привет, сыщик! Ты в особняке безумия, и тебе необходимо, ты не поверишь, найти! А вот что найти, это тебе предстоит узнать.')

	nextMessage()

	print('Выбери героя, за которого хочешь играть. Но сначала посмотри на всех.')

	nextMessage()

	choseCharacter()

	nextMessage()

	mainCharacter = input('Впиши полное имя персонажа, которого хочешь выбрать')




main()
