import pdb

print('-------------------------------------') # Separator

myString = "I love to program in Python language."

# # Example 1
file = open('.\sample_files\sample_output1.txt', 'w')

file.write(myString)

file.close()

print('-------------------------------------') # Separator

# # Example 2 
file = open('.\sample_files\sample_output1.txt', 'w')

file.write(myString)
file.write('\n')
file.write(myString + '\n')
file.write(myString)
file.write(myString)

file.close()

print('-------------------------------------') # Separator