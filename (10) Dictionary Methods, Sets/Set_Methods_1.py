# ============================================
#*=============== Set Methods ================   
# ============================================


#? clear() #?
''' Removes all elements from the set '''
# mySetFive = {1, 2, "Abdallah", "One", "Abdallah", 1}
# print(mySetFive)
# mySetFive.clear()
# print(mySetFive)

#? union() #?
''' Returns the union of sets in a new set '''
# mySetone = {1, 2, "Abdallah", "One", "Abdallah", 1,False}
# mySettwo = {5,6,7.5,False}
# print(mySetone)
# z = mySetone.union(mySettwo)
# print(z)
# print(mySetone)

#? add() #?
'''Adds an element to the set'''
# my_set = {'A',1,'B',False,2.5}
# my_set.add('C')
# print(my_set)

#? copy() #?
''' Returns a copy of the set '''
# my_set = {'A',1,'B',False,2.5}
# my_test = my_set.copy()
# my_test.clear()
# print(my_test)
# print(my_set)

#? remove() #?
''' Removes an element from the set. If the element is not a member, raises a KeyError '''
# my_set = {1,5.5,'A',True}
# print('Printing MySet Before Remove Operation: {}'.format(my_set))
# my_set.remove(5.5)
# print('Printing MySet After Remove Operation: {}'.format(my_set))
# my_set.remove('z')

#? discard() #?
''' Removes an element from the set if it is a member. (Do nothing if the element is not in set) '''
# my_set = {1,5.5,'A','Mohanad'}
# my_set.discard('16')
# my_set.discard('Mohanad')
# print(my_set)

#? pop() #?
''' Removes and returns an arbitrary set element.
   Raises KeyError if the set is empty '''

# my_set = {1,5.5,'A'}
# print(my_set.pop())
# my_set.pop()
# print(my_set)
# my_set.pop()
# # print(my_set.pop())
# print(my_set)
# my_set.pop()
# # print(my_set.pop())
# print(my_set)
# my_set.pop()

#? update() #?
''' Updates the set with the union of itself and others '''
# my_set = {1,5.5,'A'}
# my_set_2 = {5,'B',1}
# # print(my_set)
# # print(my_set_2)
# my_set_2.update(my_set)
# print(my_set_2)
