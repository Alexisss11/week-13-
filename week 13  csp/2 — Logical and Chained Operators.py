# Objective:
# Students will use logical (and, or, not) and chained comparison operators in Python to build compound conditions.

# Key Notes:

# and → Both conditions must be True

# or → At least one condition must be True

# not → Inverts True/False

# You can chain comparisons: 1 < x < 5

# Examples:
x = 10
print(x > 5 and x < 15)   # True
print(x < 5 or x == 10)   # True
print(not(x == 10))       # False
print(1 < x < 20)         # True

#score calculator
score = int(input("enter your score (0-100):"))
#if score is between 90 and 100
#assign grade A
if 90<= score <= 100:
    print("Grade: A")
#if score is between 80 and 89
# assign grade b
elif 80<= score < 90:
    print("Grade: B")

elif 70<= score < 80:
    print("Grade: C")

if 60<= score < 70:
    print("Grade: D")

elif score < 60:
    print("Grade: F") 
# Practice Problems:

# Write an expression that checks if a number is between 50 and 100 (inclusive).
num = int(input("Enter your number:"))
print(50<= num and num<=100)
# Write an expression that checks if a number is NOT equal to 0 and greater than 10.
num2 = int(input("Choose a number:"))
print(score!=0 and score > 10 )
# Use chained comparison to check if 3 < 4 < 5.
print(3<4<5)
# Challenge: Create a password rule using logical operators:
#Must be greator then 5 letters and must include a character
password = input("Enter your password:")
if len(password) >= 5 and any(char.isdigit() for char in password):
    print("Password is valid.")
else:
    print("Password is invalid.")
