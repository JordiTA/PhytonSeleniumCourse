
# Example 1
a = 20
b = 5
c = 30
d = 10

if a < b:
    print("'a' is less than 'b'.")
elif a > b and (a < c):
    print("'a' is greater than 'b'.")
else:
    print("N/A")    

print('-------------------------------------') # Separator


# Example 2
shows = ["Friends", "The Office", "Breaking Bad", "Stranger Things"]
movies = ["Rocky", "Jaws", "Batman", "Wonder Woman"]

choice = 'The Office'

if choice in shows:
    print("Your choice is a show.")
elif choice in movies:
    print("Your choice is a movie.")
else:
    print("Your choice is unknown.")

# Example 3
if (choice in shows) or (choice in movies):
    print("Your choice is valid.")
else:
    print("Unknown.")