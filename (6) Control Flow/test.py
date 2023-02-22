# name = 'alexas'
# char = input('[?] Enter Your Character: ').strip()
# print(name.find('x'))
# charIndex = name.find(char)
# print(name[:charIndex])
# print(name[charIndex+1:])
# print(name[0:name.index('x')] +name[name.index('x')+1:] )
# result = name[:charIndex] + name[charIndex+1:]
# print(f'[$] The Result --> {result}')


# ? New Way
# name = input('[?] Enter Your String: ').strip()
# char = input('[?] Enter Your Character: ').strip()
# counter = name.count(char)
# if counter == 0:
#   print('Sorry, No Characters Matches!')
# elif counter == 1:
#   result = name.replace(char,'')
#   print(f'[$] The Result --> {result}')
# else:
#   numOfChars = int(input(f'[?] How Many Times To Remove [{counter} Chars.]: '))
#   result = name.replace(char,'',numOfChars)
#   print(f'[$] The Result --> {result}')



name = input('[?] Enter Your String: ').strip()
old = input('[?] Enter Your Old String: ').strip()
counter = name.count(old)

if counter == 0:
  print('Sorry, No Matches Found!')
else:
  new = input('[?] Enter Your New String: ').strip()
  if counter == 1:
    numOfChars = 1
  else:
    numOfChars = int(input(f'[?] How Many Times To Replace [{counter} Chars.]: '))
  
  result = name.replace(old,new,numOfChars)
  print(f'[$] The Result --> {result}')