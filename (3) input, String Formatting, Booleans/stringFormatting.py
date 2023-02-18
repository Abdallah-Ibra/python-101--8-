
# ------------------------------------- 
#?-------- String Formatting ---------- 
# ------------------------------------- 
#! String concatenation: str + str = str

name = 'Alex Matt'
# print('Full Name -->',name)
# print('Full Name --> '+name)

num1 = '5'
num2 = 10
# print(type(num1),type(num2))
# print(num1+str(num2))
# print(int(num1)+num2)




name = 'Abdallah'
position = 'Python Developer'
salary = 1000

# print('Hello I am Abdallah, I am Python Developer and my Salary Rate 1000$')

# print('I am',name,'I am',position,'and My Salary is',salary,'$')
# print('I am '+name+' I am '+position+' And My Salary Rate is '+str(salary)+'$')

# %s --> str
# %d --> int
# %f --> float

print('Hello I am %s, I am %s and my Salary Rate %d$'%(name,position,salary))

print('Hello I am %s, I am %s and my Salary Rate %.2f$'%(name,position,salary))

print('Hello I am {}, I am {} and my Salary Rate {}$'.format(name,position,salary))

print(f'Hello I am {name}, I am {position} and my Salary Rate {salary}$')
