# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


print('HEY')

# phonebook = {'sam': 99912222, 'sfds': 231231, 'harry': 12299933}
# PhoneBook Capstone Project ***
phonebook = {}

size_of_array = int(input())
query_name = input()
count = 0
bad_char = [' ', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

if size_of_array > 0:

    for x in range(size_of_array):  # ask for input

        user_input = input()

        if user_input.__contains__(' ') and len(user_input) > 6:
            part_name = user_input[-8]  # Last 8 digits
            name = ''
            for letter in user_input:
                if not bad_char.__contains__(letter):
                    name.__add__(letter)
            number = user_input[-8]
            phonebook.update({name: number})

    size_of_array = 0

for i in range(size_of_array):
    if phonebook.__contains__(query_name):
        phone_num = phonebook[str(query_name)]
        print(f'{query_name}={phone_num}')
    elif not phonebook.__contains__(query_name):
        print('Not found')

