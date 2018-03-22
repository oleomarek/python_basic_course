int = -1
float = 0.2
list = ['name', 'surname']
tuple = ('name', 'sub-name')
dict =  {1:'Kuiv', 2:'Lviv'}
word = 'unit'
char = '1,version-cotrol'

#print(type(int))
'''print(type(float))
print(type(list))
print(type(tuple))
print(type(dict))
print(type(word))
print(type(char))
'''


name = input('What is your name? ')
last_name = input('What is your last name? ')
phone_number = input('Your phone nomber: ')
group = input('Your group? : ')
#print('Hello ' + name + " " + last_name + '! ' + 'You are learn in ' + group + ' and your phone: ' + phone_number + '!!!')
print(f'<{name} {last_name}>: {phone_number} - [{group}]')