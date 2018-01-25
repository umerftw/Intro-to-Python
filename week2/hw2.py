#!/usr/bin/env python

'''
The purpose of this script is to ask the user for some information and
generate a price report  and unique ID based on their inputs.

'''

# Gather the following user input and store each item as a variable: purchaser name, purchaser address,
# purchaser phone number (entered as 503-555-1211), car make/model, purchase price

user_first_name = input('What is your first name? ')
user_last_name = input('What is your last name? ')
user_address = input('What is your address? ')
user_number = input('What is your number? Please enter as XXX-XXX-XXXX: ')
car = input('What is you car make and model? ')

# price needs to be stored as float type for calculation purposes
price = float(input('How much did you purchase your car for? '))

# Calculate tax of 10% on purchase price
tax_percent = .10
tax = price * tax_percent

# Define different fees for purchasing a car
licensing_fee = float(200)
dealer_prep_fee = float(100)

# Calculate total cost
total_cost = price + tax + licensing_fee + dealer_prep_fee

# Assign last four letter's of last name to variable to form first part of unique ID
ID_part1 = user_last_name[-4:]

# Assign phone number area code to variable to form second part of unique ID
number_pieces = user_number.split("-")
ID_part2 = number_pieces[0]

# Combine variables to produce format needed for unique ID, capitalize the first part of ID
ID = "{}_{}".format(ID_part1.upper(), ID_part2)

# Print out a report

print("Hello {} {}! \nThank you for your purchase of a {}. Following is a break down of your total price: \n"
      "Sales Price: ${} \nTax: ${} \nLicensing Fee: ${} \nDealer Prep Fee: ${} \nTotal Price: ${} \nYou have "
      "been assigned an ID number of {}. Please refer to this ID number if you have any questions."
      .format(user_first_name, user_last_name, car, price, tax, licensing_fee, dealer_prep_fee, total_cost, ID))
