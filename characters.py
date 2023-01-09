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
	if mainCharacterName == 'Рита Янг':
		if special == 'health':
			return 9
		elif special == 'force':
			return 5
		elif special == 'agility':
			return 4
		elif special == 'attention':
			return 3
		elif special == 'knowledge':
			return 3
		elif special == 'communication':
			return 2
		elif  special == 'will':
			return 4
	elif mainCharacterName == 'Карсон Синклер':
		if special == 'health':
			return 8
		elif special == 'force':
			return 3
		elif special == 'agility':
			return 2
		elif  special == 'attention':
			return 5
		elif  special == 'knowledge':
			return 4
		elif  special == 'communication':
			return 4
		elif special == 'will':
			return 3
	elif mainCharacterName == 'Агата Крейн':
		if special == 'health':
			return 5
		elif special == 'force':
			return 2
		elif special == 'agility':
			return 3
		elif special == 'attention':
			return 4
		elif special == 'knowledge':
			return 5
		elif special == 'communication':
			return 3
		elif special == 'will':
			return 4
	elif mainCharacterName == 'Венди Адамс':
		if special == 'health':
			return 6
		elif special == 'force':
			return 3
		elif special == 'agility':
			return 5
		elif special == 'attention':
			return 4
		elif special == 'knowledge':
			return 3
		elif special == 'communication':
			return 3
		elif special == 'will':
			return 3
	elif mainCharacterName == 'Престон Фэрмонт':
		if special == 'health':
			return 8
		elif special == 'force':
			return 4
		elif special == 'agility':
			return 4
		elif special == 'attention':
			return 3
		elif special == 'knowledge':
			return 2
		elif special == 'communication':
			return 5
		elif special == 'will':
			return 3
	elif mainCharacterName == 'Минь Тхи Фанг':
		if special == 'health':
			return 7
		elif special == 'force':
			return 3
		elif special == 'agility':
			return 4
		elif special == 'attention':
			return 4
		elif special == 'knowledge':
			return 3
		elif special == 'communication':
			return 4
		elif special == 'will':
			return 3
	elif mainCharacterName == 'Уильям Йорик':
		if special == 'health':
			return 7
		elif special == 'force':
			return 4
		elif special == 'agility':
			return 3
		elif special == 'attention':
			return 4
		elif special == 'knowledge':
			return 3
		elif special == 'communication':
			return 3
		elif special == 'will':
			return 4
	elif mainCharacterName == 'Отец Матео':
		if special == 'health':
			return 6
		elif special == 'force':
			return 3
		elif special == 'agility':
			return 3
		elif special == 'attention':
			return 2
		elif special == 'knowledge':
			return 4
		elif special == 'communication':
			return 4
		elif special == 'will':
			return 5
