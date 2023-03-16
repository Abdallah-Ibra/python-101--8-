# -------------------------------------------------
#! ------------- Working Wtih Modules -------------
# -------------------------------------------------

#? Examples for Built-in Modules:
    #*[1] math
    #*[2] os
    #*[3] random
    #*[4] string
    #*[5] sys
    #*[6] time

#! import <module name>
#! from <module Name> import <feature>
#! from <module Name> import *

# import math
# from math import pi
# from math import *
# print(f'PI Value --> {pi}')

import os 
import time
import random
# from random import randrange as ahmed
import string


# timeNow = time.strftime("%Y/%m/%d %I:%M:%S %p")
# # get the current time in seconds since the epoch
# seconds = time.time()
# print("Seconds since epoch =", seconds)	
# # convert the time in seconds since the epoch to a readable format
# local_time = time.ctime(seconds)
# print("Local time:", local_time)

# print()
# input("Run App...")
# print('Hello World!')
# print('Hello World!')
# print('Hello World!')
# print('Hello World!')
# print('Hello World!')

# try:
#     os.system('clear')
# except:
#     os.system('cls')

# print("""
    
#         Welcome MY APP INC.
    
#     """)

# input("\n[#] Hit Any Key To close ....")


# print(random.random())
# print(random.randint(1,10))
# print(random.randrange(1,100))

# 059|8456375
# 056|8456375


# 8456375 --> random.randrange(1000,99999999)
# 8456375 --> random.randint(5120508,99999999)

# myfile = open('numbers.txt','a')
# for num in range(10000):
#     genNum = random.randint(5120508,99999999)
#     print(f'[+] Generate Number: 059{genNum}')
#     print(f'[+] Generate Number: 056{genNum}')
#     print('-'*40)
#     myfile.write(f'059{genNum}\n056{genNum}\n')

# myfile.close()
# input('[?] Hit Any Key To close..')

# with open('numbers.txt','r') as myFile:
#     data = myFile.readlines()
#     myFile.close()

# print(len(data))
# data = set(data)
# print(len(data))


# print(string.punctuation)
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# letters = list(string.ascii_letters)
# for i in range(10):
#     print(random.choice(letters))
# test = [random.choice(letters)  for i in range(8)]
# test = ''.join(test)
# print(test.title())



import names
from colorama import Fore, Back, Style,just_fix_windows_console

just_fix_windows_console()

for _ in range(10):
    fname = names.get_first_name()
    lname = names.get_last_name()
    fullName = names.get_full_name()

    print(Fore.LIGHTGREEN_EX+f'[$] First Name --> {fname}'+Fore.RESET)
    print(Fore.YELLOW+f'[$] lname Name --> {lname}'+Fore.RESET)
    print(Fore.RED+f'[$] Full Name -->  {fullName}'+Fore.RESET)
    print('=======================================')
    time.sleep(0.5)

input()