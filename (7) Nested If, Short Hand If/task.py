banner = '>>>>> Welcome To My APP <<<<<\n'
print(banner)

username = input('[?] Enter Your Username: ').strip().lower()
password = input('[?] Enter Your Password: ')

if (username == 'abdallah') and (password == 'abd12345'):
  print('\n[$] Login Successfully!')
elif (username == 'abdallah'):
  print('\n[!] Passowrd Error!')
  quit() # To Stop Our Program Here!
elif (password == 'abd12345'):
  print('\n[!] Username Error!')
  quit() # To Stop Our Program Here!
else:
  print('\n[!] Invalid Email Or Password!')
  
  quit() # To Stop Our Program Here!

print('\n||||||||| Our Services ||||||||||')
print('''
1. Remove Specific String From Text.
2. Replace Word With Word.
3. Valid Website Checker.
4. Exit.
      ''')

service = int(input('[?] Enter Your Service: '))

if service == 1:
  name = input('[?] Enter Your String: ').strip()
  char = input('[?] Enter Your Character: ').strip()
  counter = name.count(char)
  if counter == 0:
    print('[!] Sorry, No Characters Matches!')
  elif counter == 1:
    result = name.replace(char,'')
    print(f'[$] The Result --> {result}')
  else:
    numOfChars = int(input(f'[?] How Many Times To Remove [{counter} Chars.]: '))
    result = name.replace(char,'',numOfChars)
    print(f'[$] The Result --> {result}')

elif service == 2:
  name = input('[?] Enter Your String: ').strip()
  old = input('[?] Enter Your Old String: ').strip()
  counter = name.count(old)
  if counter == 0:
    print('[!] Sorry, No Matches Found!')
  else:
    new = input('[?] Enter Your New String: ').strip()
    if counter == 1:
      numOfChars = 1
    else:
      numOfChars = int(input(f'[?] How Many Times To Replace [{counter} Chars.]: '))
    
    result = name.replace(old,new,numOfChars)
    print(f'[$] The Result --> {result}')

elif service == 3:
  website = input('[?] Enter Your Website: ').strip().lower()
  endString = input('[?] Which Pattern Website Must Ends: ').strip().lower()
  startString = input('[?] Which Pattern Website Must Starts: ').strip().lower()
  if website.startswith(startString) and website.endswith(endString):
    print(f'[#] Valid Website --> [{website}]')
  else:
    print(f'[#] Invalid Website --> [{website}]')

elif service == 4:
  print('[#] See You Again..')
  quit() # To Stop Our Program Here!
else:
  print('[!] Invalid Choice, Plase Try Again!')
  quit() # To Stop Our Program Here!