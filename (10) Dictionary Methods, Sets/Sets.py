# -----------------------------
# *********** Set *************
# -----------------------------
#? [1] Set Items Are Enclosed in Curly Braces {item1, item2, item2, ...}
#? [2] Set Items Are Not Ordered 
#? [3] Set Items Are Not Indexed 
#? [4] Set Indexing and Slicing Can't Be Done
#? [5] Set Items is unchangeable (Immutable)
#? [6] Set Has Only Immutable Data Types (Numbers, Strings, Tuples), List and Dict Are Not
#? [7] Set Rejects Duplicates Items (Unique)
#* -----------------------------


#!# Not Ordered And Not Indexed ##

mySetOne = {"Ali", "Ahmed", 100}
# print(mySetOne)
# print(mySetOne[0])

#!# Slicing Can't Be Done ##

# mySetTwo = {1, 2, 3, 4, 5, 6}
# print(mySetTwo[0:3])

## Has Only Immutable Data Types ##
# mySetThree = {"Abdallah", 100, 100.5, True, [1, 2, 3]} # unhashable type: 'list'
# mySetThree = {"Abdallah", 100, 100.5, True, (1, 2, 3)}
# print(mySetThree)

## Items Unique ##
# mySetFour = {1, 2, "Abdallah", "One", "Abdallah", 1}
# print(mySetFour)

## Items is unchangeable ##
# mySetFive = {1, 2, "Abdallah", "One", "Abdallah", 1}
# # mySetFive[2] = 'Ali'
# newList = list(mySetFive)
# # print(newList)
# newList[1] = "Ali"
# print(newList)
# mySetFive = set(newList)
# print(mySetFive)
