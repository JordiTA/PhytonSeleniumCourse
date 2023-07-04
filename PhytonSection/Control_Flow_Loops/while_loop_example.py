

# #INFINITE LOOP
# boolean = True
# while boolean:
#     print('abc')

# # Example 1
counter = 1
while counter < 10:
    print(counter)
    counter = counter + 1

print('-------------------------------------') # Separator

# # Example 2
main_number = 8
user_input = None

while user_input != main_number:
    user_input = int(input("Enter a number from 0 to 10: "))
    print(f'You entered: {user_input}')

print(f"YOU WIN! Your number : {user_input} - The number to guess: {main_number}")