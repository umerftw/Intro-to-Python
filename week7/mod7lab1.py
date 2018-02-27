
from copy import deepcopy

list1 = [[1, 2, 3], ['a', 'b']]
list2 = list1

print(list1)
print(list2)

# Q1. What does list1 and list2 contain?
# The same elements

print(id(list1))
print(id(list2))

# Q2. What space in memory have list1 and list2 been assigned to?
# Are they the same?
# The same space in memory.

# setting an element to a new value
list1[0] = [5, 6, 7]
print(list1)
print(list2)
# Q3. Now what do list1 and list2 contain? What happened?
# Both lists got updated even though you only  made a change to list1.
# They contain the same elements.

list2 = list1[:]
# Q4. What does [:] in the above statement mean?
# It means do a true shallowcopy of all the elements in list1. Each element of
# list1 has now been assigned a new memory space and contained in list2

list1[0] = [2, 4, 6]
print(list1)
print(id(list1))
print(list2)
print(id(list2))

# Q5. What do list1 and list2 contain now? Why?
# They now contain different elements because the items in the two lists have
# separate memory spaces and now list1 can be changed without the same change
# being made to the elements of list2

list1[1].append('c')
print(list1)
print(list2)

# Q6. What do list1 and list2 contain now? Why?
# Both lists have been changed now to include a letter 'c'.

list2 = deepcopy(list1)
list1[1].append('x')
print(list1)
print(list2)
