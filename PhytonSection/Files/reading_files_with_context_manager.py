import pdb


print('-------------------------------------') # Separator

# # Example 1
# With closes file automatically when it ends the process.

sampleFile = '.\sample_files\programming_language_wikipedia.txt'

with open(sampleFile) as f:
    content = f.read()

# pdb.set_trace()
print(content)

print('-------------------------------------') # Separator

# # Example 2

countriesFile = '.\sample_files\list_of_countries_with_no_comma.txt'

with open(countriesFile) as f:
    countries = f.readlines()

countriesList = [i.strip() for i in countries]

# pdb.set_trace()
print(countriesList)

print('-------------------------------------') # Separator