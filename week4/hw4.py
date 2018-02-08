#!/usr/bin/env python

"""

Created by: Umer Zakaria
Date: 2/7/2018

The purpose of this code is to create a dictionary from two lists.

The user then enters a name to search within that dictionary to find the age of
the person whose name they entered.

If the name is not in the dictionary, the user can ask for a different person's age
up to five times.

"""

# create two lists
names = ["Alice", "Bob", "Cathy", "Dan", "Ed", "Frank", "Gary", "Helen", "Irene", "Jack", "Kelly", "Larry"]
ages = [20, 21, 18, 18, 19, 20, 20, 19, 19, 19, 22, 19]

# merge two lists into a dictionary
my_tuple = list(zip(names, ages))
my_dict = dict(my_tuple)

# ask user to input a name
name_input = (input('Please input an user to find out their age: '))

# output the user's age if inputted name matches a dictionary entry
# keep asking user to input a name if name inputted is not in dictionary

counter = 0
while counter < 5:
    if name_input in my_dict:
        print(my_dict[name_input])
        break
    else:
        print('User not found in database.')
        name_input = (input('Please input a different name to find out their age: '))
        counter = counter + 1
