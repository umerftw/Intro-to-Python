#!/usr/bin/env python

"""
This script will ask the user to input how many people want pizza and how many slices they want
and calculate the number of pizzas needed, how much the total cost will be, and how much each person will pay.
"""

# Create the static variables
pizza_cost = 10
slices_per_pizza = 8
tax = .096
tip = .15
delivery = 3.99

# Get user input for the following: number of people who want pizza, average number of slices per person
num_ppl = int(input('How many people want pizza? '))
avg_num = int(input('How many slices per person on average? '))

# slices = num_ppl*avg_num
# print("{} slices needed.".format(slices))


# Write function to calculate how many pizzas to order based on number of people and average slices
def num_pizza():
    slices = num_ppl * avg_num
    pizzas = round(slices/slices_per_pizza + .499)
    return pizzas


tot_pizzas = num_pizza()
print('You need to order {} pizzas.'.format(tot_pizzas))


# Write function to calculate total pizza cost
def cost():
    subtotal = tot_pizzas * pizza_cost
    total_cost = round((subtotal + (subtotal * (tax + tip)) + delivery), 2)
    return total_cost


grand_total = cost()
print('The total cost will be: ${}'.format(grand_total))


# Write function to calculate cost per person
def cost_per():
    cost_per_person = grand_total / num_ppl
    return cost_per_person


cost_person = cost_per()
print("Cost per person: ${}".format(round(cost_person, 2)))
