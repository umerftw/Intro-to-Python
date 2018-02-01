#!/usr/bin/env python

'''
Created by: Umer Zakaria
Date: 1/31/2018

The purpose of this code is to create a list based on user inputs.
The user must enter a starting value for the list higher than 1 and the
an ending value for the list that is  5 times greater than the starting value.

The user will receive an error message if those criteria are not met
and ask them to re-input a value until both the start and end values inputted
meet the requirements.

Next, the user will be given the even numbers in their list along with their
respective indices.

Finally, a sum of all the odd numbers in their created list will be displayed.

'''


# Ask the user to enter a starting and ending number
start_num = int(input('Input a starting number for your number range: '))
end_num = int(input('Input an ending number: '))

# The user must not enter a starting number less than 1
while start_num < 1:
        print('Please enter a starting number greater than 1')
        start_num = int(input('Input a starting number: '))

# The user must enter an ending number at least 5 times greater than the starting number
while end_num < 5*start_num:
        print('Please enter an ending number greater than 5 times the starting number')
        end_num = int(input('Input an ending number for your number range: '))

# Create a list of integers in the range of the user's starting and ending numbers
num_range = range(start_num, end_num)

# Print out the number and index of each item in the list that is even
for index, count in enumerate(num_range):
    if count % 2 == 0:
        print('{} is at the {}th index'.format(count, str(index)))

# Create a list of all the odd numbers in the created number range
odd_list = []
for odd_count in num_range:
    if odd_count % 2 != 0:
        odd_list.append(odd_count)

# Sum all the odd numbers in the created number range
odd_sum = sum(odd_list)

# Print that sum
print('The sum of all the odd numbers in your number range is {}'.format(odd_sum))
