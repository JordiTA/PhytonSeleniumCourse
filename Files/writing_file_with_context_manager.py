myString = "I love to program in Python language."

print('-------------------------------------') # Separator

# # Example 1

with open('.\sample_files\sample_output2.txt', 'w') as file:
    file.write(myString)

print('-------------------------------------') # Separator

# # Example 2

# myList = ['user1', 'user2', 'user3']
# with open('.\sample_files\sample_output2.txt', 'w') as file:
#     for i in myList:
#         file.write(i + '\n')

print('-------------------------------------') # Separator

# # Example 3

var2 = "Also Love Testing."

with open('.\sample_files\sample_output2.txt', 'a') as file:
    file.write('\n')
    file.write(var2)

print('-------------------------------------') # Separator

# # Example 4

languages = ['Python', 'Js', 'PHP', 'Java', 'Ruby']
with open('.\sample_files\my_fav_lenguages.csv','w') as file:

    file.writelines(languages)

print('-------------------------------------') # Separator

# # Example 5

languages = ['Python', 'Js', 'PHP', 'Java', 'Ruby']
with open('.\sample_files\my_fav_lenguages.csv','w') as file:

    file.writelines('\n'.join(languages))