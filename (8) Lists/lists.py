# ----------------------------
# ---------- Lists -----------
# ----------------------------
# [1] List Items Are Enclosed in Square Brackets
# [2] List Are Ordered, To Use Index To Access Item
# [3] List Are Mutable => Add, Delete, Edit
# [4] List Items Is Not Unique
# [5] List Can Have Different Data Types
# -----------------------------

MyList = ["Ali", "Mahmoud", "VisionPlus", 1, 100.5, True]
# print(MyList)
# print(type(MyList))

## Indexing in List ##
# print(MyList[1])  
# print(MyList[-1])  
# print(MyList[-3])  

## Slicing In List ##
# print(MyList[1:5])
# print(MyList[:4])
# print(MyList[::-1])

# print(MyList[::1]) 
# print(MyList[::2]) 

## Updating On Data ##

print(MyList)
# MyList[1] = "hi"
# print(MyList)
# MyList[-2] = 'Adnan'
# print(MyList)
# MyList[0:2] = ['Ahmed','Tariq']
# print(MyList)
MyList[0:3] = ["Welcome"]
print(MyList)
