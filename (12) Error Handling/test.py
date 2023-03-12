# try:
#     age = int(input('Enter Age: '))
# except KeyboardInterrupt:
#     exit()
# except ValueError:
#     print('[-] Error: Invalid Value,please Try Again With Valid Integer Value!')
#     age = int(input('Enter Age Again: '))

# print('[+] Age --> {}'.format(age))

for _ in range(3):
    try:
        print('='*50)
        user = input('[?] Enter Username: ').strip()
        passcode = int(input('[?] Enter Passcode: '))
        if len(user)<=10 and user.isalnum() and len(str(passcode))<=8:
            print(f'[+] Account Created --> {user}|{passcode}')
            break
        else:
            print(f'[-] Invalid Credits --> {user}|{passcode}')
    except KeyboardInterrupt:
        exit()
    # except ValueError:
    #     print('[-] Error: Enter a Valid Passcode and Username Please!')
    except Exception as err:
        print(f'[!] ERROR --> {str(err)}')
else:
    exit()


print('''

    #######################################
    ||||||||| WELCOME TO MY SPACE |||||||||
    #######################################
    ''')


