

theater_name = 'Splau Cinemas'
rated_r_age_limit = 18

print(f"Welcome to {theater_name} theaters!!!")
print("Welcome to {} theaters!!!".format(theater_name))

user_age = input("Enter your age: ")

print(f"User input is: {user_age}")

if int(user_age) >= rated_r_age_limit:
    print("Enjoy the movie!!!")
else:
    print(f"You must be {rated_r_age_limit} to watch the movie!!!")