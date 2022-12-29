def nextMessage():
	input_key = input('\n***Что бы увидеть следующее сообщение, нажми клавишу "Enter"***\n')

	while input_key != '':
		print('\n*** Это какая-то другая клавиша! ***\n')
		input_key = input('\n*** Что бы увидеть следующее сообщение, нажми клавишу "Enter" ***\n')

def lookAtCharacters():
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
		print(f'''Рита Янг
 Спортсменка
 Здоровье = {health}
 Сила = {force}
 Ловкость = {agility}
 Внимание = {attention}
 Знания = {knowledge}
 Общение = {communication}
 Воля = {will}''')

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
		print(f'''Карсон Синклер
 Дворецкий
 Здоровье = {health}
 Сила = {force}
 Ловкость = {agility}
 Внимание = {attention}
 Знания = {knowledge}
 Общение = {communication}
 Воля = {will}''')

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
		print(f'''Агата Крейн
 Парапсихолог
 Здоровье = {health}
 Сила = {force}
 Ловкость = {agility}
 Внимание = {attention}
 Знания = {knowledge}
 Общение = {communication}
 Воля = {will}''')

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
		print(f'''Венди Адамс
 Беспризорница
 Здоровье = {health}
 Сила = {force}
 Ловкость = {agility}
 Внимание = {attention}
 Знания = {knowledge}
 Общение = {communication}
 Воля = {will}''')

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
		print(f'''Престон Фэрмонт
 Миллионер
 Здоровье = {health}
 Сила = {force}
 Ловкость = {agility}
 Внимание = {attention}
 Знания = {knowledge}
 Общение = {communication}
 Воля = {will}''')

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
		print(f'''Минь Тхи Фанг
 Серкетарша
 Здоровье = {health}
 Сила = {force}
 Ловкость = {agility}
 Внимание = {attention}
 Знания = {knowledge}
 Общение = {communication}
 Воля = {will}''')

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
		print(f'''Уильям Йорик
 Могильщик
 Здоровье = {health}
 Сила = {force}
 Ловкость = {agility}
 Внимание = {attention}
 Знания = {knowledge}
 Общение = {communication}
 Воля = {will}''')

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
		print(f'''Отец Матео
 Священник
 Здоровье = {health}
 Сила = {force}
 Ловкость = {agility}
 Внимание = {attention}
 Знания = {knowledge}
 Общение = {communication}
 Воля = {will}''')

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

 #Проверка характеристик при каком-то действии

def charactersSpecialsCheck(mainCharacterName, special):
	if mainCharacterName == 'Рита Янг' and special == 'health':
		return 9
	elif mainCharacterName == 'Рита Янг' and special == 'force':
		return 5
	elif mainCharacterName == 'Рита Янг' and special == 'agility':
		return 4
	elif mainCharacterName == 'Рита Янг' and special == 'attention':
		return 3
	elif mainCharacterName == 'Рита Янг' and special == 'knowledge':
		return 3
	elif mainCharacterName == 'Рита Янг' and special == 'communication':
		return 2
	elif mainCharacterName == 'Рита Янг' and special == 'will':
		return 4
	elif mainCharacterName == 'Карсон Синклер' and special == 'health':
		return 8
	elif mainCharacterName == 'Карсон Синклер' and special == 'force':
		return 3
	elif mainCharacterName == 'Карсон Синклер' and special == 'agility':
		return 2
	elif mainCharacterName == 'Карсон Синклер' and special == 'attention':
		return 5
	elif mainCharacterName == 'Карсон Синклер' and special == 'knowledge':
		return 4
	elif mainCharacterName == 'Карсон Синклер' and special == 'communication':
		return 4
	elif mainCharacterName == 'Карсон Синклер' and special == 'will':
		return 3
	elif mainCharacterName == 'Агата Крейн' and special == 'health':
		return 5
	elif mainCharacterName == 'Агата Крейн' and special == 'force':
		return 2
	elif mainCharacterName == 'Агата Крейн' and special == 'agility':
		return 3
	elif mainCharacterName == 'Агата Крейн' and special == 'attention':
		return 4
	elif mainCharacterName == 'Агата Крейн' and special == 'knowledge':
		return 5
	elif mainCharacterName == 'Агата Крейн' and special == 'communication':
		return 3
	elif mainCharacterName == 'Агата Крейн' and special == 'will':
		return 4
	elif mainCharacterName == 'Венди Адамс' and special == 'health':
		return 6
	elif mainCharacterName == 'Венди Адамс' and special == 'force':
		return 3
	elif mainCharacterName == 'Венди Адамс' and special == 'agility':
		return 5
	elif mainCharacterName == 'Венди Адамс' and special == 'attention':
		return 4
	elif mainCharacterName == 'Венди Адамс' and special == 'knowledge':
		return 3
	elif mainCharacterName == 'Венди Адамс' and special == 'communication':
		return 3
	elif mainCharacterName == 'Венди Адамс' and special == 'will':
		return 3
	elif mainCharacterName == 'Престон Фэрмонт' and special == 'health':
		return 8
	elif mainCharacterName == 'Престон Фэрмонт' and special == 'force':
		return 4
	elif mainCharacterName == 'Престон Фэрмонт' and special == 'agility':
		return 4
	elif mainCharacterName == 'Престон Фэрмонт' and special == 'attention':
		return 3
	elif mainCharacterName == 'Престон Фэрмонт' and special == 'knowledge':
		return 2
	elif mainCharacterName == 'Престон Фэрмонт' and special == 'communication':
		return 5
	elif mainCharacterName == 'Престон Фэрмонт' and special == 'will':
		return 3
	elif mainCharacterName == 'Минь Тхи Фанг' and special == 'health':
		return 7
	elif mainCharacterName == 'Минь Тхи Фанг' and special == 'force':
		return 3
	elif mainCharacterName == 'Минь Тхи Фанг' and special == 'agility':
		return 4
	elif mainCharacterName == 'Минь Тхи Фанг' and special == 'attention':
		return 4
	elif mainCharacterName == 'Минь Тхи Фанг' and special == 'knowledge':
		return 3
	elif mainCharacterName == 'Минь Тхи Фанг' and special == 'communication':
		return 4
	elif mainCharacterName == 'Минь Тхи Фанг' and special == 'will':
		return 3
	elif mainCharacterName == 'Уильям Йорик' and special == 'health':
		return 7
	elif mainCharacterName == 'Уильям Йорик' and special == 'force':
		return 4
	elif mainCharacterName == 'Уильям Йорик' and special == 'agility':
		return 3
	elif mainCharacterName == 'Уильям Йорик' and special == 'attention':
		return 4
	elif mainCharacterName == 'Уильям Йорик' and special == 'knowledge':
		return 3
	elif mainCharacterName == 'Уильям Йорик' and special == 'communication':
		return 3
	elif mainCharacterName == 'Уильям Йорик' and special == 'will':
		return 4
	elif mainCharacterName == 'Отец Матео' and special == 'health':
		return 6
	elif mainCharacterName == 'Отец Матео' and special == 'force':
		return 3
	elif mainCharacterName == 'Отец Матео' and special == 'agility':
		return 3
	elif mainCharacterName == 'Отец Матео' and special == 'attention':
		return 2
	elif mainCharacterName == 'Отец Матео' and special == 'knowledge':
		return 4
	elif mainCharacterName == 'Отец Матео' and special == 'communication':
		return 4
	elif mainCharacterName == 'Отец Матео' and special == 'will':
		return 5
