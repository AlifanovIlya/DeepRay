def next_message():
	input_key = input('***Что бы увидеть следующее сообщение, нажми клавишу "Enter"***\n')

	while input_key != '':
		print('*** Это какая-то другая клавиша! ***')
		input_key = input('*** Что бы увидеть следующее сообщение, нажми клавишу "Enter" ***\n')

def character_direction(character_direction_choice):
	if character_direction_choice == 'Юг' or character_direction_choice == 'юг':
		return('Юг')
	elif character_direction_choice == 'Север' or character_direction_choice == 'север':
		return('Север')
	elif character_direction_choice == 'Запад' or character_direction_choice == 'запад':
		return('Запад')
	elif character_direction_choice == 'Восток' or character_direction_choice == 'восток':
		return('Восток')
	else:
		return('Что-то другое')

def inventory_update():
	print('*** Инвентарь обновлен! ***')

print('Проснулся наконец? Я думал, ты уже не встанешь.\n')

next_message()

character__started_local = input('Привет, из какого ты города?\n')
print(character__started_local + '? Не слышал о таких местах.\n')

character_name = input('А как зовут тебя, помнишь?\n')
print('Рад знакомству, ' + character_name + ' из ' + character__started_local)

next_message()

character_direction_first = input('Куда ты хочешь пойти? На Юг? Север? Запад или Восток?\n')
if character_direction(character_direction_first) == 'Юг':
	print('О, это нам по пути!\n')
elif character_direction(character_direction_first) == 'Север':
	print('Интереный выбор, но там холодно!\n')
elif character_direction(character_direction_first) == 'Запад':
	print('Хорошо, можно и туда.\n')
elif character_direction(character_direction_first) == 'Восток':
	print('Ладно, ступай своей дорогой.\n')
elif character_direction(character_direction_first) == 'Что-то другое':
	print('Я тебя не понимаю.\n')
else:
	print('Я тебя не понимаюю\n')

next_message()

print('Какой класс ты хочешь выбрать?.\n')

inventory_update()
print('*** +1 Старый меч. ***\n')
