import json

with open('phonebook.json') as json_file:
	data = json.load(json_file)
for p in data['phonebook']:
	print('Name: ' + p['name'])
	print('Surname: ' + p['surname'])
	print('Number: ' + p['number'])
	print('')

choice = raw_input("Co chcesz zrobic? d - dodac, u -usunac: ")
if choice == "d":
	name = raw_input("Write name: ")
	surname = raw_input("Write surname: ")
	number = raw_input("Write number: ")
	data['phonebook'].append({
		"name" : name,
		"surname" : surname,
		"number" : number
		})
if choice == "u":
	delChoice = raw_input("Podaj, ktory wpis usunac (1 - pierwszy wpis, 2 -drugi itd.) :")
	del data['phonebook'][int(delChoice)-1]
with open('phonebook.json', 'w') as outfile:
    json.dump(data, outfile)
