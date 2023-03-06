# ============================================
#*=============== Set Methods ================   
# ============================================


#? issuperset() #?
''' Returns True if this set contains another set '''

a = {1, 2, 3, 4,5}
b = {1, 2, 3}
# # c = {1, 2, 3, 4, 5}

# print(a.issuperset(b))  # True
# print(b.issuperset(a))  # False
# print(a.issuperset(c))  # False

#? issubset() #?
''' Returns True if another set contains this set '''
# d = {1, 2, 3, 4}
# e = {1, 2, 3}
# f = {1, 2, 3, 4, 5}

# print(d.issubset(e))  # False
# print(e.issubset(d))  # True

# print(d.issubset(f))  # True

#? isdisjoint() #?
''' Returns True if two sets have a null intersection '''

g = {1, 2, 3, 4}
h = {1, 2, 3}
i = {10, 11, 12}

# print(g.isdisjoint(h))  # False
# print(g.isdisjoint(i))  # True