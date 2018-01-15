#!/usr/bin/env python

'''
The purpose of this script is to ask the user for three inputs and use them
to output a single sentence made of a combination of those inputs.

Please take no offense to the outputted sentence.
'''

# ask user for their name
user_name = input("You there! What is your name? ")

# ask user for favorite food
fav_food = input("What is your favorite food? ")

# ask user how often they've eaten that favorite food
food_freq = input("How many times have you eaten it in the last year? ")

# output a combined sentenced with a string operation
print("Look here,", user_name+".", " They say you are what you eat and you definitely look like you've eaten", fav_food,
      food_freq, "times. Let's just take a step back?")
