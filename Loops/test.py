# role = 'Guest'
# while (role == 'guest'.title()):
#     print('Go Back Guest!')



# counter = 1
# #         11   <= 10 --> False
# while (counter <= 10):
#     print(f'[{str(counter).zfill(2)}] Hello World')
#     # counter = counter + 1 
#     counter+=1 #? increament Operator
#     # counter-=1 #? decreament Operator


#? Task
# from pprint import pprint
# print('''
    
#     >>>>> Welcome To My App <<<<<<
    
#     ''')
# counter = int(input("[?] Enter the Number Of Entries: "))
# x = 0
# people = {}
# while counter > 0:
#     x +=1
#     print(f'\n[#] Person({str(x).zfill(2)}) Details: ')
#     name = input('  [?] Enter The Name: ').strip().title()
#     age = int(input('  [?] Enter The Age: '))
#     ident = int(input('  [?] Enter the ID: '))
#     counter -= 1
#     print('-'*40)
#     people.update({
#         f'Person{x}':{
#             'name':f'{name}',
#             'age':f'{age}',
#             'id':f'{ident}',
#             }
#         })

# print(f'[$] All Data: \n\n')
# pprint(people)
# '''
# {
#     'Person1': {'name': 'Ahmed', 'age': '23', 'id': '934838483'},
#     'Person2': {'name': 'Mohammed', 'age': '19', 'id': '3493847346'},
#     'Person3': {'name': 'Alex', 'age': '20', 'id': '3847394834'}
# }
# '''




# tries = 3
# validUser,validPassword = 'admin','admin'
# while (tries > 0):
#   username = input('[?] Enter Your Username: ').strip()
#   password = input('[?] Enter Your Password: ')
#   if username == validUser and password == validPassword:
#     print("يا ويلكم")
#     print('''
#         >>>>>> Welcome To Premium App <<<<<<<
#       ''')
#     # input("Hit Any Key To Close!")
#     break
#   else:
#     print("العب بعييد يلااا")

#   tries -=1
#   print(f'\n---------- [Still {tries} Tries]  ----------')


# name = 'Abdallah'
# names = ['Amir','Ahmed','joudy','Essaa','Yousef']
# for name in names:
#     # print(f'Hello, It is Pleasure To There Please {name.title()}')
#     print('Hi')


# VIPL12345
# for t in range(100):
#     print(f"Your ID --> VIPL{str(t+1).zfill(5)}")



name = 'Joudy'
newName = []
for char in name:
    # print(char)
    if char.strip().lower() == 'j' or char.strip().lower() == 'd':
        pass
        # print('Prevent Printing, May Contains "j" or "d" Char!')
    else:
        print(char)
        newName.append(char)



print(f"New Name --> {''.join(newName)}")