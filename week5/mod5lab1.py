# # Read the file into a list
#
# with open('land_time_forgot.txt') as f:
#     infile = f.readlines()
#     length = int(len(infile))
#     length1of3 = int(length / 3)
# #    print("There are {} lines in this book.".format(length))
#     length2of3 = length1of3 + length1of3
#     middle = infile[length1of3:length2of3]
#     midlength = len(middle)
# #    print("There are {} lines in the middle third of this book.".format(midlength))
#     line1 = infile[length1of3]
#     line2 = infile[length2of3]
# #    print('The line that appears one third of the way through the book is "{}". The line that appears two-thirds'
# #          ' of the way through this book is "{}"'.format(line1, line2))
#
# with open('output.txt', 'w') as f:
#     f.write(line1)
#     f.write(line2)

# Convert the list of book lines into a list of the words (hint: use a for loop and list.extend OR two for loops
# and list.append)
words = []
for line in open('land_time_forgot.txt'):
    words.extend(line.split(" "))

print('This book has {} words.'.format(len(words)))

with open('land_time_forgot.txt') as f:
    lines = f.readlines()

first_line = lines[0]
print(first_line)

project_title, author = first_line.split(", by ")
print('The title of the book is {}.'.format(project_title))
print('The author of the book is {}.'.format(author))
