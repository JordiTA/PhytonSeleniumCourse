import pdb

print('-------------------------------------') # Separator

sampleFile = '.\sample_files\programming_language_wikipedia.txt'

# # Example 1

# file = open(sampleFile)
# content = file.read()
# file.close()
# contentList = content.split("\n\n")

print('-------------------------------------') # Separator

# # Example 2
# readline() only read the first line
file = open(sampleFile)
content = file.readline()
file.close()

print(content)

print('-------------------------------------') # Separator

# # Example 3
# readlines() Returns a list with all the lines
file = open(sampleFile)
content = file.readlines()
file.close()

print(content)

print('-------------------------------------') # Separator

# # Example 4
# seek() if we read the file twice without closing it
file = open(sampleFile)

content = file.read()
print("1-----")
print(content)

file.seek(0)

content2 = file.read()
print("2-----")
print(content2)

file.close()

print('-------------------------------------') # Separator