

theater_name = 'Splau Cinemas'
rated_r_age_limit = 18

print(f"Welcome to {theater_name} theaters!!!") # py3
print("Welcome to {} theaters!!!".format(theater_name)) # py3 & py2

user_age = input("Enter your age: ")

print(f"User input is: {user_age}")

if int(user_age) >= rated_r_age_limit:
    print("Enjoy the movie!!!")
else:
    adult_present = input("Is an adult present? (yes/no) ")
    if adult_present.lower() == 'yes':
        print("Enjoy the movie!!!")
    else:
        print(f"You must be {rated_r_age_limit} to watch the movie!!!")