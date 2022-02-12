# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


""" Objective
Today, we're learning about Key-Value pair mappings using a Map or Dictionary data structure. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given
names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. You will then be given an unknown number of names to query your phone book for. For each queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; if an entry for

is not found, print Not found instead.

Note: Your phone book should be a Dictionary/Map/HashMap data structure.

Input Format

The first line contains an integer,
, denoting the number of entries in the phone book.
Each of the subsequent lines describes an entry in the form of space-separated values on a single line. The first value is a friend's name, and the second value is an

-digit phone number.

After the
lines of phone book entries, there are an unknown number of lines of queries. Each line (query) contains a

to look up, and you must continue reading lines until there is no more input.

Note: Names consist of lowercase English alphabetic letters and are first names only. """


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

