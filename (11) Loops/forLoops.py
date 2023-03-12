
#?-------------------------------------?#
#!------------- for Loops -------------!# 
#?-------------------------------------?#


#* For Loops Form:

'''
for varName in iterableData:
   Expression

! Notes:
? varName --> Any Vriable name will values stored in it all loops run.
? iterableData --> Any Datatypes You Iterate on it , like strings, lists, dictionaries and tuples.
? Expression --> Will Excutes while it is possible to iterating through itarable data.
'''


## Iterating Over List ##

my_list = [1,'VisionPlus','Hi','Apple',False]

# for stuff in my_list:
# #   # print(type(i))
#    print(stuff)
#   print(f"Value ==> {stuff}, Type ==> {type(stuff)}")


## Use range() Method ##

# for x in range(30):
#    # print(x)
#    print(f'[{x+1}] Hello From VisionPlus!')



### Using enumerate() Function ###
# funny_list = ['Banana','Apple','Student','Teacher','Manager','Fruits']
# print(type(x))

# for z,y in enumerate(funny_list):
#    print(f'{z+1}. {y}')
   

## Nested For ##
# Students = ["Jaber", "Ahmed", "Rahaf"]
# skills = ['Java', 'Python', 'PHP']

# for stud in Students:
#    print(f"[*] {stud}: ")
#    for skill in skills:
#       print(f'\t- {skill}')
#    print('='*30)



## For Loop With Dictionary ##

developers = {
   'Jaber':'Python',
   'Ahmed':'Java',
   'Rahaf':'PHP'
   }

# {key:value}
# print(developers.get("Rahaf"))
# print(developers['Rahaf'])
# print(developers.keys())
# print(developers.values())
# print(developers.items())

# dev,lang = ("Rahaf","Python")

x = 0
for key,value in developers.items():
   print(f'[{x+1}] {key} ==> {value}')
   x +=1

# for key in developers:
#    print(key)

# for key in developers.keys():
#    print(key)

# for value in developers.values():
#    print(value)


# for key, value in developers.items():
#    print(key, value)


