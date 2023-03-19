from colorama import Fore
import sys,time


def go(sub,details):
    print('''
    1. Show Student Details
    2. Show Marks Info
    3. Register Subject
    4. Remove Subject 
    5. Show Finincial Details
    6. Leave Gateway
    
        '''+Fore.MAGENTA)

    try:
        ask = int(input('[?] Enter Your Choice (1-6): '))
        if ask == 1:
            print('[#] Student Details: ')
            print(Fore.YELLOW+details.read().title()+Fore.RESET)
            time.sleep(1)
        elif ask == 2:
            print('[#] Show Marks Info: ')
            allSubs = sub.readlines()
            for i in allSubs:
                name,mark,hrCount,hrCost = i.strip().split('|')
                print(Fore.RESET+'\n ---------------------------------')
                print(Fore.CYAN+f'  [+] Subject Name: {name.title()}'+Fore.RESET)
                print(Fore.CYAN+f'  [+] Subject Mark: {mark}/100'+Fore.RESET)
                print(Fore.CYAN+f'  [+] Count Hours: {hrCount} Hours'+Fore.RESET)
                print(Fore.CYAN+f'  [+] Cost Per Hour: {hrCost}$'+Fore.RESET)
                time.sleep(0.5)
            print('\n')
            time.sleep(1)
        elif ask == 3:
            subject = input('[?] Enter Subject Name: ')
            subMark = input('[?] Enter Subject Mark: ')
            hours = input('[?] Enter The Number of Hours: ')
            cost = input('[?] Enter The Cost For Hour: ')
            with open('./20161897/subjects.txt','a') as sus:
                sus.write(f'{subject}|{subMark}|{hours}|{cost}\n')
            
            time.sleep(1)
        elif ask == 4:
            print('[#] Remove Subject Operation..')
            subName = input('[?] Enter Subject Name To Remove: ').strip()
            allSubs = sub.readlines()
            subIndex = 0
            subFound = False
            for s in allSubs:
                if str(s).strip().lower().startswith(f"{str(subName).lower()}"):
                    subFound = True
                    break
                subIndex+=1
            if subFound:
                z = allSubs.pop(subIndex)
                print(Fore.LIGHTGREEN_EX+f'[+] \"{str(z).split("|")[0]}\" Subject Removed Successfully.'+Fore.RESET)
            else:
                print(Fore.RED+f'[!] "{subName}" Not Found!'+Fore.RESET)
            time.sleep(1)
        elif ask == 5:
            print('[#] Show Finincial Details')
            print('------------------------------')
            print('| Subject Name | Total Costs |')
            print('------------------------------')
            total = 0
            allSubs = sub.readlines()
            for i in allSubs:
                name,mark,hrCount,hrCost = i.strip().split('|')
                total += int(hrCount)*float(hrCost)
                print(f'|  {Fore.CYAN}{name.title()}{Fore.RESET}: {Fore.CYAN}{int(hrCount)*float(hrCost)}${Fore.RESET}')
                print('------------------------------')
                time.sleep(0.5)
            print(f'|\t{Fore.LIGHTGREEN_EX}Total = {total}${Fore.RESET}')
            print('------------------------------')
            time.sleep(1)
        elif ask == 6:
            print('[#] See You Again..')
            time.sleep(1)
            sys.exit()
        else:
            print(Fore.RED+'[-] Error: Enter a valid choice (1-6).'+Fore.RESET)
            time.sleep(1)
        
    except Exception as e:
        print(Fore.RED+f'[-] Error: {e}'+Fore.RESET)
    except KeyboardInterrupt:
        sys.exit()


banner = Fore.BLUE+r'''
   +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   +  ___      ___  __      ________  __      ______    _____  ___   + 
   + |"  \    /"  ||" \    /"       )|" \    /    " \  (\"   \|"  \  + 
   +  \   \  //  / ||  |  (:   \___/ ||  |  // ____  \ |.\\   \    | + 
   +   \\  \/. ./  |:  |   \___  \   |:  | /  /    ) :)|: \.   \\  | + 
   +    \.    //   |.  |    __/  \\  |.  |(: (____/ // |.  \    \. | + 
   +     \\   /    /\  |\  /" \   :) /\  |\\        /  |    \    \ | + 
   +      \__/    (__\_|_)(_______/ (__\_|_)\"_____/    \___|\____\) + 
   +                                                                 +
   +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

'''+Fore.RESET
print(banner)
creditsFile = open('./20161897/crediontials.txt','r')

acceptedUser = False
user,passs = creditsFile.readline().split(':')
for _ in range(3):
    try:
        username = input("[?] Enter Username: ")
        password = input("[?] Enter Password: ")
        if (username.strip() == user.strip()) and (password == passs):
            print(Fore.LIGHTGREEN_EX+'[+] Login Successfully,redirecting You in Moments..\n'+Fore.RESET)
            time.sleep(1)
            acceptedUser = True
            break
        else:
            print(Fore.RED+'[-] Invalid Credintionls!\n'+Fore.RESET)
            time.sleep(1)
    except KeyboardInterrupt:
        sys.exit()


if acceptedUser:
    while True:
        subjectsFile = open('./20161897/subjects.txt','r')
        detailsFile = open('./20161897/deatils.txt','r')
        go(subjectsFile,detailsFile)
        subjectsFile.close()
        detailsFile.close()


creditsFile.close()
