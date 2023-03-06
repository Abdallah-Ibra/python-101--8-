# ------------------------
# -- Dictionary Methods --
# ------------------------

# clear()

# user = {
#   "name": "Osama"
# }
# print(user)
# user.clear()
# print(user)

# print("=" * 50)

# update()

# member = {
#   "name": "Abd"
# }
# print(member)
# member["age"] = 24
# print(member)
# member.update({"country": "Palestine","age": "23"})
# print(member)

# print("=" * 50)

# # copy()

main = {
  "name": "Abd"
}

# b = main.copy()
# print(b)
# main.update({"skills": "Play Music"})
# print(main)
# print(b)

# keys() + values()

# print(main.keys())
# print(main.values())

# setdefault()

# user = {
#   "name": "Abd"
# }
# print(user)
# print(user.setdefault("age", 24))
# print(user)

# print("=" * 40)

# popitem()

# member = {
#   "name": "Abd",
#   "skill": "PS4"
# }
# print(member)
# member.update({"age": 24})
# print(member.popitem())
# print(member.popitem())
# print(member.popitem())
# print(member.popitem())

# print("=" * 40)

# # items()

# view = {
#   "name": "Abd",
#   "skill": "XBox"
# }

# allItems = view.items()
# print(view)
# view["age"] = 36

# print(allItems)

# print("=" * 40)

# fromkeys()

a = ('MyKeyOne', 'MyKeyTwo', 'MyKeyThree')
b = "X","Z","Y"

print(dict.fromkeys(a, b))