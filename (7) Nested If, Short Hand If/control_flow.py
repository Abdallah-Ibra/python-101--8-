
#?---------------------------------------------?#
#!------ Control Flow (if, elif, else) --------!#
#*---------------------------------------------*#

#?# Before We Learn If Condition, let's revise Comparasion Operartors ...
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
#* These conditions can be used in several ways, most commonly in "if statements" and loops.


#!# Python If Statement Syntax #!#

'''
if test expresion:
    statement(s)
''' 
# num = int(input("Enter The Number: "))

# if (num > 0):
#     print("Positive Number!")
# else:
#     print("Negative Number!")



# print("=========== My APP =============")
# username = input("[+] Username: ").strip()
# phone_number = input("[+] Phone Number: ").strip()
        
#         ## True ##                                     ## True ##
# if (not username.isnumeric()) and (len(phone_number) >= 10 and len(phone_number) < 15):
#     print("Login Succeassfully..")
# else:
#     print("check your username or phone number!")

# print("\n")
# print(f"Username ==> {username}")
# print(f"Phone Number ==> {phone_number}")

# if not username.isnumeric():
#     print("Valid Username..")
# else:
#     print("Please Enter A Valid Username!")
    
# if len(phone_number) >= 10 and len(phone_number) < 15:
#     print("Valid Phone Number...")
# else:
#     print("Please Enter A Valid Phone Number!")


## Example 2 ##
# username = input('Enter Your Username: ').strip().capitalize()
# phone_number = input('Enter Your Phone Number: ').strip()

# if username.isnumeric(): ## Check if username is valid or not (valid username have at least one string char.)
#    print('Error! Please Enter a Valid Username [ex.abd681]..')
#    ## Code ##
# if len(phone_number) < 8 or len(phone_number) > 15: ## The Validated Phone Number Must Be longer than 8 and less than 15 chars
#    print('Error! Please Enter The Valid Phone Number[ex.9874563210]..')
## Code ## 


#!# Python if...else Statement Syntax #!#

'''
if test expression:
    Body of if
else:
    Body of else
'''

# Try these two variations as well. 
# num = -5
# num = 0
# num = -1

# if num > 0:
#    print("Positive Number")
# else:
#    print("Negative number")



#!# Python if..elif..else Statement Syntax #!#

'''
if test expression:
    Body of if
elif another test expression:
    Body of elif
else:
    Body of else
'''
## Example 1 ##

num = 10
# Try these two variations as well:
# num = 0
# num = -4.5

# if num > 0:
#    print("Positive number")
# elif num == 0:
#    print("Zero")
# else:
#    print("Negative number")
# if num > 0:
#    print("Positive number")

# if num < 0:
#    print("Negative number")

# if num == 0:
#    print("Zero")


#?# Using 'and', 'or', '!=' with if condithion #?#

# And
# The and keyword is a logical operator, and is used to combine conditional statements:
# Example
# Test if a is greater than b, AND if c is greater than a:

# a = 200
# b = 33
# c = 500
# if a > b and a < c:
#    print("Both conditions are True")

# if ( b < a < c):
#    print("Both are True")


# Or
# The or keyword is a logical operator, and is used to combine conditional statements:
# Example
# Test if a is greater than b, OR if a is greater than c:

# a = 200
# b = 33
# c = 500
# if a > b or a > c:
#    print("At least one of the conditions is True")



# The pass Statement
# if statements cannot be empty, 
# but if you for some reason have an if statement with no content, 
# put in the pass statement to avoid getting an error.

a = 33
b = 200

# if b != a:
#    pass
# else:
#    print("Important Text!")

# if a == b:
#    print("Important Text!")

# print("This is Another Statement!")



## Nested if  ##
num = int(input("Enter Your Number: "))

if num == 0:
    print("Zero!")
else:
    if num > 0:
        print("Positive Number!")
    elif num < 0:
        print("Negative Number!")
    
    