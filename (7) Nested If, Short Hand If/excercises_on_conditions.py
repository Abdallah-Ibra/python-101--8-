### Conditions Exercises ###
#! Python Program to Check if a Number Odd or Even
#! Python Program to Find The Largest Among Three Numbers
#! Python Program to Check Leap Year
# -----------------------------------------------------------




######## First APP ########
# Even number == عدد زوجي
# Odd number == عدد فردي

# 4/2 = 2 , 0  ==> Even Number
# 3/2 = 1 , 1 ==> Odd Number

# print("""
#                >>>>>> Hello World <<<<<<

#    "This is a Simple Program to Check if Number is Odd or Even" 
#       """)


# Even ==> x %2 == 0
# Odd ==> x %2 !=0

# number = int(input("Enter Your Number: "))

# if number == 0:
#       print("Zero!")
# elif number % 2 == 0:
#       print(f'{number} ==> Even Number')
# else:
#    print(f'{number} ==> Odd Number')

# if number != 0:
#       # Short Hand IF #
#       print(f"{number} --> Even!") if number %2==0 else print(f'{number} --> Odd!')
# else:
#       print("Zero Number!")

# if number == 0:
#       print("Zero!")
# else:
#    if number %2 == 0:
#          print("Even Number!")
#    else:
#          print("Odd Number!")



# num_one=float(input("Enter number one: "))
# num_two=float(input("Enter number two: "))
# num_three=float(input("Enter number three: "))

# if num_one == num_two and num_one == num_three:
#    print("All Numbers Are Equals!")
# else:
#    if(num_one > num_two) and (num_one > num_three):
#       print(f"{num_one} --> is the largest")
#    elif(num_two > num_one) and (num_two > num_three):
#       print(f"{num_two} --> is the largest")
#    else:
#       print(f"{num_three} --> is the largest")







# ######### Second APP #########


# num1 = float(input('Enter Number1 : '))
# num2 = float(input('Enter Number2 : '))
# num3 = float(input('Enter Number3 : '))
# if num1 > num2 and num1 > num3 :
#    print(num1)
# elif num2 > num1 and num2 > num3:
#    print(num2)
# elif num3 > num1 and num3 > num2:
#    print(num3)
# else:
#    if num1 == num2 or num2 == num3 or num1 == num3:
#       print('Two Numbers Are Equals!')
#    else:
#       print('All Equals Other!')



######### Third APP #########

## What Is a Leap Year? 

# Leap years are years where an extra, or intercalary, day is added to the end of the shortest month, February.
# The intercalary day, February 29, is commonly referred to as leap day.
# Leap years have 366 days instead of the usual 365 days and occur almost every four years.

### السنة الكبيسة هي السنة التي تقبل القسمة على 4 باستثناء أرقام السنوات التي تنتهي ب100 إلا في حال قبولها القسمة على 400
## سنة 1900 ليست سنة كبيسة بناء على الشروط السابقة
## سنة 2000 سنة كبيسة 
## سنة 2100 و سنة 2200 وسنة 2300 فلن تكون سنوات كبيسة

year = int(input("[?] Enter The Year: "))


if year % 4 != 0:
      print(f"{year} --> Not Leap Year!")
else:
      if year % 100 ==0:
            if year %400 ==0:
                  print(f"{year} --> Leap Year!")
            else:
                  print(f" {year} --> Not Leap Year!")
      else:
            print(f"{year} -->  Not Leap Year!")


# if (year % 4) == 0:
#    if (year % 100) == 0:
#       if (year % 400) == 0:
#          print(f'{year} is a Leap Year')
#       else:
#          print(f'{year} is not a Leap Year')
#    else:
#       print(f'{year} is not a Leap Year')
# else:
#    print(f'{year} is not a Leap Year')

