
# ---------------------------
#! ----- Dictionary ---------
# ---------------------------
# [1] Dict Items Are Enclosed in Curly Braces {}
# [2] Dict Items Are Contains Key : Value
# [3] Dict Key Need To Be Immutable => (Number, String, Tuple) List Not Allowed
# [4] Dict Value Can Have Any Data Types
# [5] Dict Key Need To Be Unique
# [6] Dict Is Not Ordered You Access Its Element With Key
# ----------------------------

# Dictionary

user = {
  "name": "Adnan",
  "age": 23,
  "country": "Palestine",
  "skills": ["Html", "Css", "JS"],
  "rating": 10.5,
  }

# print(type(user))
# print(f'[+] Name ==> {user["name"]}')
# print(f"[+] Age ==> {user['age']}")
# print(f"[+] Country ==> {user['country']}")
# print(f"[+] Skills ==> {user['skills']}")
# print(f"[+] Rating ==> user['rating']")

# print(f"I'm {user['name']}, my age is {user.get('age')} and I am from {user.get('country')}")

# print(f"User Keys ==> {user.keys()}")
# print("+"*50)
# print(f"User Values: {user.values()}")

# Two-Dimensional Dictionary
languages = {
  
  "One": {
    "name": "Html",
    "progress": "80%",
  },

  "Two": {
    "name": "Css",
    "progress": "90%"
  },

  "Three": {
    "name": "Js",
    "progress": "90%"
  },

}

# print(languages)
# print(languages['One'])
# print(languages.get("Two"))
# print(languages['Three']['name'])

# Dictionary Length

# print(len(languages))
# print(len(languages["Two"]))

# Create Dictionary From Variables

frameworkOne = {
  "name": "Vuejs",
  "progress": "80%"
}

frameworkTwo = {
  "name": "ReactJs",
  "progress": "80%"
}

frameworkThree = {
  "name": "Angular",
  "progress": "80%"
}

# print(frameworkOne)
# print(frameworkTwo)
# print(frameworkThree)

allFramework = {
  "one": frameworkOne,
  "two": frameworkTwo,
  "three": frameworkThree
}

print(allFramework)