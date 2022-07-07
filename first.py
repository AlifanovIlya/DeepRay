def next_message():
	input_key = input('***Что бы увидеть следующее сообщение, нажми клавишу "Enter"***\n')

	while input_key != '':
		print('*** Это какая-то другая клавиша! ***\n')
		input_key = input('*** Что бы увидеть следующее сообщение, нажми клавишу "Enter" ***\n')

def character_direction(character_direction_choice):
	for i in character_direction_choice:
		if i == 'Ю' or i == 'ю':
			return('South')
			break
		if i == 'С' or i == 'с':
			return('North')
			break
		if i == 'З' or i == 'з':
			return('West')
			break
		if i == 'В' or i == 'в':
			return('East')
			break

def character_class(character_class_choise):
	for i in character_class_choise:
		if i == 'М' or i == 'м':
			#for j in character_class_choise:
				#if j == 'Ч' or i == 'ч':
			return('Swordman')
			break
		if i == 'Л' or i == 'л':
			return('Bowner')
			break
		if i == 'Г' or i == 'Г':
			return('Mage')
			break

def inventory_update():
	print('*** Инвентарь обновлен! ***\n')

print('Проснулся наконец? Я думал, ты уже не встанешь.\n')

next_message()

character__started_local = input('Привет, из какого ты города?\n')
print(character__started_local + '? Не слышал о таких местах.\n')

character_name = input('А как зовут тебя, помнишь?\n')
print('Рад знакомству, ' + character_name + ' из ' + character__started_local + '\n')

next_message()

character_direction_first_choise = input('Куда ты хочешь пойти? На Юг? Север? Запад или Восток?\n')
if character_direction(character_direction_first_choise) == 'South':
	print('О, это нам по пути!\n')
elif character_direction(character_direction_first_choise) == 'North':
	print('Интереный выбор, но там холодно!\n')
elif character_direction(character_direction_first_choise) == 'West':
	print('Хорошо, можно и туда.\n')
elif character_direction(character_direction_first_choise) == 'East':
	print('Ладно, ступай своей дорогой.\n')
else:
	print('Я тебя не понимаюю\n')

next_message()

character_class_first_choise = input('Какой класс ты хочешь выбрать?.\n')
if character_class(character_class_first_choise) == 'Swordman':
	print('Ммм, любишь помахать большой железной штукой? Ну держи, пригодиться.\n')
	inventory_update()
	print('*** +1 Старый меч. ***\n')
elif character_class(character_class_first_choise) == 'Bowner':
	print('Любитель поразить цель издалека? Вот, держи, он доольно не плох.\n')
	inventory_update()
	print('*** +1 Длинный деревянный Лук. ***\n')
elif character_class(character_class_first_choise) == 'Mage':
	print('Так ты предпочитаешь решать проблемы "словами"? Вот тебе книжка с заклинаниями.\n')
	inventory_update()
	print('*** +1 Старый альмонах ***\n')
else:
	print('Странный класс, мне нечего тебе предложить.\n')