def getDetails(name,age,hairColor):
  print(f'[+] Name: {name}')
  print(f'[+] Age: {age}')
  print(f'[+] Hair Color: {hairColor}')
  print('-'*30)


newList = []
for i in range(3):
  
  print(f'\n--------- Person ({i+1}) ---------')
  name = input('[?] Enter Your Name: ')
  age = int(input('[?] Enter Your Age: '))
  hairColor = input('[?] Enter Your Hair Color: ')
  newList.append(f'{name}:{age}:{hairColor}')

# print(newList)
print('\n---------- Show Details -----------')
for x in newList:
  # print(x)
  # details = x.split(':')
  # getDetails(details[0],details[1],details[2])
  name,age,hair = x.split(':')
  getDetails(name,age,hair)