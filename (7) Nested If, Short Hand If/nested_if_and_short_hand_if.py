
#?-----------------------------------------?#
#!------ Nested if & Short Hand If --------!#
#*-----------------------------------------*#

## Example on nested if ##

# num = float(input("Enter a number: "))

# if num == 0:
#     print('Zero Number!')
# elif num > 0 :
#     print('Positive Number!')
# else:
#     print('Negative Numeber!')


# if num >= 0:
#     if num > 0:
#         print('Positive Number!')
#     else:
#         print('Zero!')
# else:
#     print('Negative!')
# ----------------------------------------

# age = 30
# if age > 40:
#     print('Sorry, You Are Rejected!')
# else:
#     if age < 18:
#         print('Sorry, You Are Too Young!')
#     else:
#         print('You Are Accepted!')







## Short Hand If ##
# If you have only one statement to execute, you can put it on the same line as the if statement.

a = 2
b = 330

# if a > b:
#     print('A')
# else:
#     print('B')

# Short Hand If [Ternanry If] #
# Expr.1 if condtion1 else Expr.2
# print("A") if (a > b) else print("B")



# name = input("Enter Your Name: ")
# tall = int(input("Enter Your Tall: "))

# print(f"Welcome {name}, you are Accepted!") if (tall >= 170) else print("You are Rejected!")



# # a = 170
# name = input("Enter Your Name: ")
# tall = int(input("Enter Your Tall Average: "))
# wieght = int(input("Enter Your Weight: "))

# if tall >= 170 and  (60 <= wieght <= 85):
#     print(f'Welcome {name.title()},You Are Accepted!')
# else:
#     print(f'Welcome {name.title()},You Are Rejected!')

# print(f'Hello Mr {name},You are Accepted!') if a >= 170 else print("Sorry, You Are rejected!")

# print(f'Hello Mr {name}, You are Taller Than or equals {a}')

# This technique is known as Ternary Operators, or Conditional Expressions.
# Short Hand If ... Else

# If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:
# One line if else statement, with 3 conditions:
a = 90
b = 10

# if a > b:
#     print("A")
# else:
#     if a == b:
#         print("A == B")
#     else:
#         print("B")


print('A') if (a>b) else print('Equals') if (a == b) else print('B')
