# print('Hello World!')
# print('Hello World!')
# print('Hello World!')

# def sayHi():
#     # print('Hello World!')
#     return 'Hello World!'

# x = sayHi()
# print(x)
# for _ in range(10):
#     sayHi()
import sys
from colorama import Fore,just_fix_windows_console
just_fix_windows_console()

def sum(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def multi(num1,num2):
    return num1*num2

def div(x,y):
    return x/y




print('''

    [1] Sum
    [2] Subtraction
    [3] multiplication
    [4] Division
    [5] Exit
    ''')

oper = int(input('[?] Enter Your opertor: '))
num1 = float(input('[?] Enter Number1: '))
num2 = float(input('[?] Enter Number2: '))
if oper == 1:
    print(sum(num1,num2))
elif oper == 2:
    print(sub(num1,num2))
elif oper == 3:
    print(multi(num1,num2))
elif oper == 4:
    print(div(num1,num2))
else:
    exit()

# while True:
#     try:
#         num1 = float(input('[?] Enter Number1: '))
#         num2 = float(input('[?] Enter Number2: '))
#         result = num1+num2
#         # print(f'[+] Result: {result}')
#         print(f'{Fore.LIGHTGREEN_EX}Result --> {Fore.YELLOW}{num1}{Fore.LIGHTGREEN_EX} + {Fore.YELLOW}{num2}{Fore.LIGHTGREEN_EX} = {Fore.LIGHTMAGENTA_EX}{result}{Fore.RESET}')
#         print('='*50)
#     except KeyboardInterrupt:
#         print(Fore.RED+'\n[#] See You Again...'+Fore.RESET)
#         sys.exit()
#     except Exception as e:
#         print(Fore.RED+f'[-] ERROR --> {e}'+Fore.RESET)