print('-------------------------------------') # Separator
# # Example of 'random' module
# https://docs.python.org/3/library/random.html

import random

number1 = random.randint(100,200)
print(number1)
number2 = random.randrange(3)
print(number2)

print('-------------------------------------') # Separator

mainList = ['aaa', 'bbb', 'ccc', 'ddd']
print(f"Original List: {mainList}")

random.shuffle(mainList)
print(f"Random Shuffle: {mainList}")

choiceList = random.choice(mainList)
print(f"Random Choice: {choiceList}")

sampleList = random.sample(mainList,2)
print(f"Random Sample(Pick X items from a list): {sampleList}")

print('-------------------------------------') # Separator