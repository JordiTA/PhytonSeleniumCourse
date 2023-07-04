# main_number = 15
# user_input = None

# while user_input != main_number:
#     user_input = int(input("Enter a number from 0 to 20: "))
#     print(f'You entered: {user_input}')

# print(f"YOU WIN! Your number : {user_input} - The number to guess: {main_number}")

main_number = 15
user_input = None

# # Example 1
while True:
    user_input = int(input("Enter a number from 0 to 20: "))
    print(f'You entered: {user_input}')
    if user_input == main_number:
        break

print(f"YOU WIN! Your number : {user_input} - The number to guess: {main_number}")

print('-------------------------------------') # Separator

# # Example 2
# Given a country print its capital city if it is given in the set of data, else print 'unknown'
capitals = {
    "Peru": "Lima",
    "Philippines": "Manila",
    "Spain": "Madrid",
    "Ethiopia": "Addis Ababa",
    "Ghana": "Accra"
}

user_input = 'spain'

for country, capital in capitals.items():
    print("Current country: " + country)
    if user_input.lower() == country.lower():
        print("Capital is: " + capital)
        break

print('-------------------------------------') # Separator

# # Example 3
# given a dictionary with book prices and list of courses, calculate total cost of books
book_prices = {
    "calculus": 300,
    "physics": 255,
    "chemistry": 400,
    "english": 150,
    "theater": 100
}

total_cost = 0

my_courses = ["physics", "english", "psychology", "calculus", "history"]

for course in my_courses:
    if course not in book_prices.keys():
        continue
    total_cost += book_prices[course]
    total_cost = total_cost + book_prices[course]

print("Total books cost: {}".format(total_cost))