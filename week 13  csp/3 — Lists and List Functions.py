# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.
#collection = single "variable" used to store multiple values
#list = [] ordere4d and changeable, dupllicates are OK
# set = {} unordered and immutable, but Add/remove OK, No duplicates
# Tuple = () ordered and unchangable. Duplicates OK FASTER
#list are ordered collections of items
# list are 
# instead of storing a bunch of variables you can stopre them in a list
# This makes our job easier when we need to manage multiples items 
# performance task answer
my_list1= ['1', '2', '3', '4', '5']
print(my_list1)
print(my_list1[0])
print(my_list1[0:4])
print(my_list1)
print(my_list1[-1])
# Examples:
my_list1.extend([10,11,12,13,14])
print(my_list1)
# add 500 more numbers to the list
my_list1.extend(list(range(15, 515)))
print(my_list1)
my_list1.extend(list(range(515, 1115)))
print(my_list1)

my_list = ['apple', 'banana', 'cherry']
print(my_list[0])         # apple
print(my_list[1:])        # ['banana', 'cherry']

my_list.append('grape')
print(my_list)

my_list.pop(1)
print(my_list)

numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)


# Practice Problems:

# Create a list with 5 of your favorite foods.
list2 = ['cookies', 'coffee', 'beans', 'steak', 'karissa']
# Print the second and last item.
print(list2[3:])
# Add a new item using .append().

# Remove the first item using .pop(0).

# Reverse your list using .reverse().

# Create a list of 3 lists (matrix), and access the middle element.