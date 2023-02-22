
#?---------------------------------------------?#
#!------ Control Flow (if, elif, else) --------!#
#*---------------------------------------------*#

# ?# Before We Learn If Condition, let's revise Comparasion Operartors ...
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
# * These conditions can be used in several ways, most commonly in "if statements" and loops.


# ---------------------------------------------------------

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

# ---------------------------------------------------------

# name = input('[?] Enter Your Name Please: ').strip().lower()

# if (name == 'abdallah'):
#    print('Welcome Home Developer {}'.format(name.title()))  # This Will Excute if Condition is True
# else:
#    print('Welcome Guest!')  # This Will Excute if The First Condition is False

# print('This is Another Sentence!')


# drink = 'Cola'

# station1 = 'found'
# station2 = 'found'
# station3 = 'not found'
# if station1 == 'found':
#    print('I Got it From Station1!')
# print('Come Back!')
# if station2 == 'found':
#    print('I Got it From Station2!')
# print('Come Back!')
# if station3 == 'found':
#    print('I Got it From Station3!')
# print('Come Back!')
# print('Take a break!')


# drink = 'Cola'
# station1 = 'not found'
# station2 = 'not found'
# station3 = 'not found'

# if (station1 == 'found'):
#    print('Got it from Station1!')
# elif (station2 =='found'):
#    print('I got it from Station2!')
# elif (station3 =='found'):
#    print('I got it from Station3!')
# else:
#    print('Not Found!')

# print("Take a break!")


# Usernaame --> len(username) >= 5
# Email --> Contains '@'


# username = 'abed123'.strip()
# email = 'emptyone4stuff@gmail.com'.strip().lower()


# if (len(username) >=5) and  '@' in email:
#    print("Login Successfully!")
# else:
#    print("Invalid Username or Email!")

# if (len(username) >=5) and  '@' in email:
#    print("Login Successfully!")
# elif len(username) >= 5:
#    print("Valid Usenrame but Email is Wrong!")
# elif '@' in email:
#    print("Valid Email but username is Wrong!")
# else:
#    print("Invalid Username or Email!")


# if (len(username) >= 5):
#    print('[+] Valid Username.')
# else:
#    print('[!] Invalid Username.')

# if '@' in email:
# if (email.find('@') != -1):
#    print("[+] Valid Email.")
# else:
#    print("[!] Invalid Email.")


# mark = int(input('Enter Your Mark: '))

# if (mark > 100) or (mark <= 0):
#    print('Invalid Mark!')
# elif (mark >= 90):
#    print("Excellent!")
# elif (mark >= 80):
#    print("Very Good!")
# elif (mark >= 70):
#    print("Good!")
# elif (mark >= 50):
#    print('Pass!')
# else:
#    print("Fail!")


website = input('Enter Your Website: ').strip().lower()

if (website.startswith('www.') or website.startswith('https://') or website.startswith('http://')) and website.endswith('.ps'):
    print("[+] Valid URL --> {}".format(website))
else:
    print("[-] Invalid URL --> {}".format(website))
