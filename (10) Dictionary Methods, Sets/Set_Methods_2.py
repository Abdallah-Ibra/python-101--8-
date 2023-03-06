# ============================================
#*=============== Set Methods ================   
# ============================================


#? difference() #?
''' Returns the difference of two or more sets as a new set '''
my_set_1 = {'apple','banna','orange'}
my_set_2 = {'orange','juice','ahed'}

# print(f"my_set_1 Before ==> {my_set_1}")
# print(f"my_set_2 Before ==> {my_set_2}")
# dif_set_1 = my_set_1.difference(my_set_2)
# dif_set_2 = my_set_2.difference(my_set_1)
# print(dif_set_1)
# print(dif_set_2)
# print(f"my_set_1 After ==> {my_set_1}")
# print(f"my_set_2 After ==> {my_set_2}")``

#? difference_update() #?
''' Returns the difference of two or more sets as a new set '''
# my_set_1 = {'apple','banana','orange'}
# my_set_2 = {'orange','juice','ahed'}
# print(f"my_set_1 Before ==> {my_set_1}")
# print(f"my_set_2 Before ==> {my_set_2}")
# dif_set_1 = my_set_1.difference_update(my_set_2)
# dif_set_2 = my_set_2.difference_update(my_set_1)

# print(dif_set_1)
# print(dif_set_2)
# print("-"*30)
# print(f"my_set_1 After ==> {my_set_1}")
# print(f"my_set_2 After ==> {my_set_2}")


#? intersection() #?
''' Returns the intersection of two sets as a new set '''

my_set_1 = {1,5.5,'Mohanad',6,11}
my_set_2 = {1,5,'Adnan',6,11}
# x = my_set_1 & my_set_2
# print(x)
# print(my_set_1)
# print(my_set_2)

# x = my_set_1.intersection(my_set_2)
# y = my_set_2.intersection(my_set_1)
# print(x)
# print(my_set_1)
# print(y)



#? intersection_update() #?
''' Updates the set with the intersection of itself and another '''
my_set_1 = {1,5.5,'Mohanad',6,11}
my_set_2 = {1,5,'Adnan',6,11}
# print(my_set_1)
# print(my_set_2)
# my_set_1.intersection_update(my_set_2)
# my_set_2.intersection_update(my_set_1)
# print(my_set_1)
# print(my_set_2)

#? symmetric_difference() #?
''' Returns the symmetric difference of two sets as a new set '''
# my_set_1 = {1,5.5,'Mohanad',6,11}
# my_set_2 = {1,5,'Adnan',6,11}
# x = my_set_1.symmetric_difference(my_set_2)
# print(x)
# x = my_set_1 ^ my_set_2
# print(x)

#? symmetric_difference_update() #?
''' Updates a set with the symmetric difference of itself and another '''

my_set_1 = {1,5.5,'Mohanad',6,11}
my_set_2 = {1,5,'Adnan',6,11}
my_set_1.symmetric_difference_update(my_set_2)
print(my_set_1)