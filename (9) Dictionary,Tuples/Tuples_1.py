# -----------------------------------------
# **************** Tuples ****************** 
# -----------------------------------------
#? [1] Tuple Items Are Enclosed in Parentheses (item1, item2, item3,...)
#? [2] You Can Remove The Parentheses If You Want
#? [3] Tuple is Ordered
#? [4] Tuple is unchangeable (Immutable)
#? [5] Tuple Allow Duplicates
#? [6] Tuple Can Have Different Data Types
#? [7] Operators Used in Strings and Lists Available In Tuples
#? [8] Tuples are used to store multiple items in a single variable
#* -----------------------------


### Tuple Syntax and Type ###

''' Here We W'll See Tuple Syntax and Type of it , not the the difference between string datatype and tuple datatype when you write it with single value '''
# Empty Tuple #
# my_tuple= ()
# print(type(my_tuple))
# Mixed Datatype #
# my_tuple1 = ('Adnan',1,2.5,True,['Alex',2.5,False],('p',5,3.5))
# my_tuple2 = ('Adnan',)
# print(my_tuple1)
# print(type(my_tuple2))

### Tuple Indexing ###
''' In This Zone We w'll See That We Can get any Item from tuple by using .index() function '''
# my_tuple = ('Adnan',1,2.5,True,['Alex',2.5,False],('p',5,3.5,["Ahmed",3]))
# print(my_tuple[-1][-1][0])
# print(my_tuple[-2][1])
# my_tuple[-2][1] = 5
# print(my_tuple[-2][1])


### Tuple Slicing ###
''''  Here We W'll Access To multu values using slicing '''
# my_tuple = ('Adnan',1,2.5,True,['Alex',2.5,False],('p',5,3.5))
# print(my_tuple[1:5])
# print(my_tuple[-4:-1])

### Tuple Assign Values ###
''' Here We W'll Notice That We Can Assign any value on any items on the Tuple '''
   # TypeError: 'tuple' object does not support item assignment
   # However, item of mutable element can be changed (ex. lists)
# my_tuple = ('Adnan',1,2.5,True,['Alex',2.5,False],('p',5,3.5))
# my_tuple[1] = False
# print(my_tuple) ## Type Error!

### Duplicates Data in Tuple ###
''' Here We W'll Add Duplicates Data and see that our tuple accepts it '''
# my_tuple = ('Adnan',1,2.5,True,['Alex',2.5,False],('p',5,3.5),'Adnan')
# print(my_tuple)

### Deleting Tuple ###
   # can't delete items
   # TypeError: 'tuple' object doesn't support item deletion
   # But We can delete an entire tuple using (del entire_tuple)
# my_tuple = ('Adnan',1,2.5,True,['Alex',2.5,False],('p',5,3.5),'Adnan')
# del my_tuple
# print(my_tuple)



### Since We Can't Change Any items values in tuple, but in fact, we can change any items in it
### ! by converting tuples to list and access any element and then change any value!
my_tuple = ("M",5,0.5,True)
print(f"Type Before: {type(my_tuple)}")


my_tuple= list(my_tuple)
print(f"Type After: {type(my_tuple)}")
my_tuple.append("Helloo")
print(f"Printing After Appending ==> {my_tuple}")
# print(my_tuple[1])
my_tuple[1] = 10
# print(my_tuple)
my_tuple = tuple(my_tuple)
print(my_tuple)