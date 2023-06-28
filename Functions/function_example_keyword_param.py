print('-------------------------------------') # Separator

# # Example 1
# Write a function that will return number of words that have X length, given a string

def getSmallWordsCount(inputString, maxSize=3):

    smallWords = []

    for word in inputString.split():
        if len(word) <= maxSize:
            smallWords.append(word)
    
    return len(smallWords)

joke = "In Python hashtags are used to tell the computer a line is not worth reading. Much like social media."

smallWordsCount = getSmallWordsCount(joke)
print(smallWordsCount)

smallWordsCount = getSmallWordsCount(joke, 4)
print(smallWordsCount)

print('-------------------------------------') # Separator

# # Example 2
# 
def connectDatabase(host='test.db.com', username='testuser', password='testpass'):
    print(f"Connection to host: {host}")
    print(f"Username : {username}")

connectDatabase('prod.db.com', 'JordiUserName', 'secrete')

print('-------------------------------------') # Separator