

# # Example 1
my_list = ['house', 'car', 'bike', 'boat']

for i in my_list:
    print(i)
    print('----------------------')

fruits = ['Orange', 'Apple', 'Banana']
for j in fruits:
    print(j)

print('-------------------------------------') # Separator

# # Example 2
# Print out words that are 3 or less characters
quote = "Give a man a program, frustate him for a day. Teach a man to program, frustate him for a lifetime"

for i in quote.split():
    if len(i) <= 3:
        print(i)
    else:
        pass

print('-------------------------------------') # Separator

# # Example 3
# Collect the small words (3 or less characters) into a list and print the list
quote = "Give a man a program, frustate him for a day. Teach a man to program, frustate him for a lifetime"

small_words = []

for i in quote.split():
    if len(i) <= 3:
        small_words.append(i)

print(small_words)

print('-------------------------------------') # Separator

# What happens if you loop an empty list?
empty_list = []

for i in empty_list:
    print(i)

# Nothing, it does not produce any error.
