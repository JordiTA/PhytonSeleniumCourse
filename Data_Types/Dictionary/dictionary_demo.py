

capitals = {"Spain":"Madrid", "France":"Paris", "Turkey":"Ankara"}

# # Get items from a dictionary
france_capital = capitals["France"]
print(france_capital)

france_capital_ = capitals.get("France")
print(france_capital_)

print('-------------------------------------') # Separator

# # Get key that does not exist : ERRORKEY
# ethiopia_capital = capitals["Ethiopia"]

# # Get key that does not exist : NONE
# ethiopia_capital = capitals.get("Ethiopia")
# print(ethiopia_capital)

# return a default value if key does not exist 
ethiopia_capital2 = capitals.get("Ethiopia", "NOT EXIST LOSER")
print(ethiopia_capital2)

print('-------------------------------------') # Separator

# # Add item to dictionary
print("Before adding:")
print(capitals)

# Option 1
capitals["Kenya"] = "Nairobi"
print("After Option 1:")
print(capitals)

# Option 2
capitals.update({"India":"New Delhi"})
print("After Option 2:")
print(capitals)

# Option 3
capitals.setdefault("England","London")
print(capitals)

print('-------------------------------------') # Separator

capitals_keys = capitals.keys()
capitals_values = capitals.values()
print(capitals_keys)
print(capitals_values)

print('-------------------------------------') # Separator

# # Another example of a dictionary

employee = {"name": "Jordi Tomas",
            "age": 22,
            "phone": 684934763,
            "title": "Mr. No One",
            "skills": ["AWS", "Python", "Java", "C++"]
            }
e_name = employee['name']
e_age = employee['age']
e_skills = employee['skills']
print(type(e_skills))
user_skill_count = len(e_skills)
print(f"User has {user_skill_count} skills.")
print("User has {} skills".format(user_skill_count))