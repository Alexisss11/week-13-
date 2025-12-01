
list1 = [1,2,3]
list2 = [4,5,6]
nested_list = [list1, list2]
print(nested_list)
print(nested_list[1][2]) #output 6
print(nested_list[0][1]) #output 2
fruits = ["apple", "orange", "bannana", "coconut" ]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chichekn", "fish", "turekey"]
groceries = [fruits, vegetables, meats]
print(groceries[1][2])
print(groceries[0])
print(groceries[1])
print(groceries[2])
print(groceries[0][3]) #output is coconut
print(groceries[0][2])

groceries = ["apple", "orange", "bannana", "coconut" ], ["celery", "carrots", "potatoes"], ["chichekn", "fish", "turekey"]
for collection in groceries:
   for food in collection:
    print(food, end=" " )
    print()

# num_pad = ((1, 2, 3),
#     (4, 5, 6),
#     (7, 8, 9),
#     ("*", 0, "#"))

# for row in num_pad:
#     for num in row:
#     print(num, end=" ")
#     print()
# # Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# Examples:Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# Examples:

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])    # 6
print(matrix[0][2])

# List comprehension
first_col = [row[0] for row in matrix]
print(first_col)       # [1, 4, 7]
example_list = [row[0]for row in matrix]
#for row in matrix print(row[0])
print(example_list)


# Practice Problems:

# Build a matrix variable containing 3 lists of 3 numbers each.

matrix2 = [
    [3, 2, 3],
    [2, 0, 6],
    [18, 8, 4]
]
# Print the first list.
print(matrix2[0])
# Print the second item from the third list.
print(matrix2[2][1])
# Use a list comprehension to extract the last item from each sub-list.
com_list = [row[2] for row in matrix2]
print(com_list)
# Challenge: Create a new list containing squares of numbers from 1–10 using a comprehension. 
squared_numbers = [x**2 for x in range (1,11)]
#for x in range (1, 11) : squared = x**2 print(squared_numbers)
print(squared_numbers)