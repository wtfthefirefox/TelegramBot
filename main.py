import gspread
from oauth2client.service_account import ServiceAccountCredentials
import config
import telebot

scope					 = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds					 = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client					 = gspread.authorize(creds)

def findYouStudents(date, id):
	dictOfCurStudens = {}
	if (sheets[id].title[0] != '_'):
		sheet			 = sheets[id]
		row			 = sheet.row_values(1)
		del row[0]
		del row[0]

		if (len(row) != 0):
			for col in range(0, len(row)): # Dates
				if (row[col] == date): # Check date == column
					column	 = sheet.col_values(col + 3)
					del column[0]

					if (len(column) != 0):
						for r in range(0, len(column)): # Columns
							
							if (column[r] != ''):
								dictOfCurStudens[f'{r + 1}'] = sheet.cell(r + 2, 2).value

		if (len(dictOfCurStudens) == 0):
			return ''
		else:
			return dictOfCurStudens
	return ''

def createDictOfCurStudents(date, idWT):
	dictA = findYouStudents(date, idWT)

	if (dictA == ''):
		return 0
	else:
		if (sheets[idWT].title[0] != '_'):
			return {
				'group': f'{sheets[idWT].title[len(sheets[idWT].title) - 1]}',
				'studens': findYouStudents(date, idWT)}

def findName(idName, idGroup):
	for sh in sheets:
		if (sh.title[len(sh.title) - 1] == str(idGroup) and sh.title[0] != '_'):
			return sh.cell(idName + 1, 2).value

def createStrOfStuends(grp): # grp type int
	string = ''
	sheets = client.open('Bonuses').worksheets()

	for sh in sheets:
		if (sh.title[len(sh.title) - 1] == str(grp) and sh.title[0] != '_'):
			column = sh.col_values(2)
			del column[0]

			for i in range(0, len(column)):
				string += f'{i + 1}: {column[i]}\n'

			return string

def listOfStudens(id):
	sheets = client.open('Bonuses').worksheets()

	for sh in sheets:
		if (sh.title[len(sh.title) - 1] == str(id) and sh.title[0] != '_'):
			column = sh.col_values(2)
			del column[0]
			return column

def createArrOfStd(time): 
	string = ''
	sheets = client.open('Bonuses').worksheets()
	arr = []

	for sh in sheets:
		if (sh.title[0] != '_'):
			rows = sh.row_values(1)
			del rows[0]
			del rows[0]

			for r in range(0, len(rows)):
				if (rows[r] == time):
					column = sh.col_values(2)
					row = sh.col_values(r + 3)
					del column[0]
					del row[0]

					for i in range(0, len(row)):
						if(row[i] != ''):
							arr.append(column[i])

	return arr

def createArrRightStd(name, arr):
	arrStd = arr.copy()

	for a in arrStd:
		if (a == name):
			arrStd.remove(a)

	return arrStd

def createStrRightStd(arr):	
	s = ''

	for i in range(0, len(arr)):
		s += f'{i + 1}: {arr[i]}\n'

	return s		

sheets = client.open('Bonuses').worksheets()

bot = telebot.TeleBot()

@bot.message_handler(commands=['start'])
def exchange_command(message):

	keyboard = telebot.types.InlineKeyboardMarkup()
	keyboard.row(
		telebot.types.InlineKeyboardButton('161', callback_data=161),
		telebot.types.InlineKeyboardButton('162', callback_data=162),
		telebot.types.InlineKeyboardButton('163', callback_data=163),
		telebot.types.InlineKeyboardButton('164', callback_data=164),
		telebot.types.InlineKeyboardButton('165', callback_data=165)
	)

	bot.send_message(message.chat.id, 'Из какой ты группы?', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
	bot.answer_callback_query(callback_query_id=call.id, text='Спасибо за честный ответ!')

	if (161 <= int(call.data) <= 165):
		answer = ''

		if call.data == '161':
			if (open("config.py", encoding = "utf8").read() == ''):
				open("config.py", encoding = "utf8").close()
				d = {call.message.chat.id: {
						'group': '1'
					}
				}
			else:
				d = config.dictOfStudens

				d[call.message.chat.id] = {
					'group': '1'
				}

			with open("config.py", "w", encoding = "utf8") as file:
				file.write(f'dictOfStudens = {d}')

			data = createStrOfStuends(1)

			answer = 'Ура вы из 161!\n' + 'Введите свой номер по списку\n' + data

		elif call.data == '162':
			if (open("config.py", encoding = "utf8").read() == ''):
				open("config.py", encoding = "utf8").close()
				d = {call.message.chat.id: {
						'group': '2'
					}
				}
			else:
				d = config.dictOfStudens

				d[call.message.chat.id] = {
					'group': '2'
				}

			with open("config.py", "w", encoding = "utf8") as file:
				file.write(f'dictOfStudens = {d}')

			data = createStrOfStuends(2)

			answer = 'Ура вы из 162!\n' + 'Введите свой номер по списку\n' + data

		elif call.data == '163':
			if (open("config.py", encoding = "utf8").read() == ''):
				open("config.py", encoding = "utf8").close()
				d = {call.message.chat.id: {
						'group': '3'
					}
				}
			else:
				d = config.dictOfStudens

				d[call.message.chat.id] = {
					'group': '3'
				}

			with open("config.py", "w", encoding = "utf8") as file:
				file.write(f'dictOfStudens = {d}')

			data = createStrOfStuends(3)

			answer = 'Ура вы из 163!\n' + 'Введите свой номер по списку\n' + data

		elif call.data == '164':
			if (open("config.py", encoding = "utf8").read() == ''):
				open("config.py", encoding = "utf8").close()
				d = {call.message.chat.id: {
						'group': '4'
					}
				}
			else:
				d = config.dictOfStudens

				d[call.message.chat.id] = {
					'group': '4'
				}

			with open("config.py", "w", encoding = "utf8") as file:
				file.write(f'dictOfStudens = {d}')

			data = createStrOfStuends(4)

			answer = 'Ура вы из 164!\n' + 'Введите свой номер по списку\n' + data

		elif call.data == '165':
			if (open("config.py", encoding = "utf8").read() == ''):
				open("config.py", encoding = "utf8").close()
				d = {call.message.chat.id: {
						'group': '5'
					}
				}
			else:
				d = config.dictOfStudens

				d[call.message.chat.id] = {
					'group': '5'
				}

			with open("config.py", "w", encoding = "utf8") as file:
				file.write(f'dictOfStudens = {d}')

			data = createStrOfStuends(5)

			answer = 'Ура вы из 165!\n' + 'Введите свой номер по списку\n' + data

		bot.send_message(call.message.chat.id, answer)

	bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
	if (1 <= int(call.data) <= 2):
		if (call.data == '1' and len(config.dictOfStudens[call.message.chat.id]) == 2):
			d = config.dictOfStudens
			d[call.message.chat.id]['name'] = findName(int(d[call.message.chat.id]['number']), int(d[call.message.chat.id]['group']))

			with open("config.py", "w", encoding = "utf8") as file:
				file.write(f'dictOfStudens = {d}')

		elif (call.data == '2' or len(config.dictOfStudens[call.message.chat.id]) == 3):
			s = config.dictOfStudens[call.message.chat.id]['group']

			fString = createStrOfStuends(int(s))
			bot.send_message(call.message.chat.id, f'Введите свой номер по списку\n {fString}')

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
	try:
		d = config.dictOfStudens
		if (message.text.isdigit() == True and 1 <= len(d[message.chat.id]) <= 2 and d[message.chat.id]['group'].isdigit()):
			s = listOfStudens(int(d[message.chat.id]['group']))
			if (1 <= int(message.text) <= len(s)):
				c = 0
				g = 0
				flag = -1
				if (len(d.keys()) == 1):
					flag = 1
				else:
					for key in d.keys():
						if (len(d[key]) == 3 and d[key]['number'] != message.text):
							c += 1
					for key in d.keys():
						if (len(d[key]) == 3):
							g += 1

				if (c == g or flag == 1):
					keyboard = telebot.types.InlineKeyboardMarkup()
					keyboard.row(
						telebot.types.InlineKeyboardButton('Да', callback_data=1),
						telebot.types.InlineKeyboardButton('Нет', callback_data=2),
					)

					d[message.chat.id]['number'] = message.text

					with open("config.py", "w", encoding ="utf8") as file:
						file.write(f'dictOfStudens = {d}')
					
					idGrp = d[message.chat.id]['group']

					bot.send_message(message.chat.id, f'Вы {findName(int(message.text), int(idGrp))}?', reply_markup = keyboard)
				else:
					bot.send_message(message.chat.id, f'Этот человек уже зарегистрирован')
			else:
				bot.send_message(message.chat.id, f'Вы неправильно ввели свой номер по списку!')
	except KeyError:
		bot.send_message(message.chat.id, 'Вы ещё не выбрали свою группу!')

	# Start voting
	if (message.text.split(' ')[0] == '123'): # Password
		if(len(open("config.py", encoding = "utf8").read().split('\n\n')) == 1):
			open("config.py", encoding = "utf8").close()

			arrOfCurStudents = []

			for sh in range(0, len(sheets)): # Open new list
				dictSh = createDictOfCurStudents(message.text.split(' ')[1], sh)
				if (dictSh != 0):
					arrOfCurStudents.append(dictSh)

			dictOfStd = config.dictOfStudens
			newDict = {}

			for keyD in dictOfStd.keys():
				for element in range(0, len(arrOfCurStudents)):
					if (dictOfStd[keyD]['group'] == arrOfCurStudents[element]['group']):
						for key, val in arrOfCurStudents[element]['studens'].items():
							if (dictOfStd[keyD]['name'] == val and dictOfStd[keyD]['number'] == key):
								newDict[dictOfStd[keyD]['name']] = keyD

			with open("config.py", "w", encoding = "utf8") as file:
				file.write(f'dictOfStudens = {dictOfStd}\n\ncurrencyStudens = {newDict}')

			with open("output/date.txt", "w", encoding = "utf8") as file:
				file.write(message.text.split(' ')[1])
		else:
			open("config.py", encoding = "utf8").close()
			
		arr = config.currencyStudens

		arrStd = createArrOfStd(message.text.split(' ')[1])

		for val in arr.values():
			data = createStrRightStd(createArrRightStd(config.dictOfStudens[val]['name'], arrStd))
			bot.send_message(val, f'Пожалуйста, выберете того человека, которому вы отдадите свой балл:\n{data}')

		dictStd = {name: 0 for name in arrStd}

		if (len(open("config.py", encoding = "utf8").read().split('\n\n')) == 2):
			open("config.py", encoding = "utf8").close()
			with open("config.py", encoding = "utf8") as file:
				string = file.read()
			with open("config.py", "w", encoding = "utf8") as file:
				file.write(f'{string}\n\nresultsOfInterview = {dictStd}')
		else:
			open("config.py", encoding = "utf8").close()

		NewDict = {val: key for key, val in arr.items()}

		with open("config.py", encoding = "utf8") as file:
			string = file.read()
		with open("config.py", "w", encoding = "utf8") as file:
			file.write(f'{string}\n\ncheckYourVote = {NewDict}')
	# Voting
	if (len(message.text.split(' ')) == 1 and message.text.isdigit() and len(open('config.py', encoding = "utf8").read().split('\n\n')) == 4 and len(config.dictOfStudens[message.chat.id].keys()) == 3 and 1 <= int(message.text) <= len((config.resultsOfInterview).keys())):
		open('config.py', encoding = "utf8").close()

		d = config.checkYourVote

		if(d[message.chat.id] != ''):
			with open("output/date.txt", encoding = "utf8") as file:
				arrStd = createArrOfStd(file.read())

			if (1 <= int(message.text) <= len(arrStd)):

				data = createArrRightStd(config.dictOfStudens[message.chat.id]['name'], arrStd)

				if (1 <= int(message.text) <= len(data)):

					arr = config.resultsOfInterview
					arr[data[int(message.text) - 1]] += 1

					d[message.chat.id] = ''

					with open('config.py', encoding = "utf8") as file:
						spl = file.read().split('\n\n')

					spl[2] = f'resultsOfInterview = {arr}'
					d = config.checkYourVote
					d[message.chat.id] = ''
					spl[3] = f'checkYourVote = {d}'

					with open('config.py', "w", encoding = "utf8") as file:
						file.write(f'{spl[0]}\n\n{spl[1]}\n\n{spl[2]}\n\n{spl[3]}')

					bot.send_message(message.chat.id, "Спасибо за ваш голос!")	
		else:
			bot.send_message(message.chat.id, "Вы уже проголосовали!")	

	# Stop voting
	if(message.text == 'STOP' and message.chat.id == 490492546 and len(open('config.py', encoding = "utf8").read().split('\n\n')) == 4):
		open('config.py', encoding = "utf8").close()

		arr = config.resultsOfInterview
		data = ''

		for val, key in arr.items():
			data += f'{val}: {key}\n'

		arr = config.currencyStudens

		for val in arr.values():
			bot.send_message(val, data)

		bot.send_message(490492546, data)

		arr = config.dictOfStudens

		with open('config.py', "w", encoding = "utf8") as file:
			file.write(f'dictOfStudens = {arr}')

bot.polling(none_stop=True, interval=0)