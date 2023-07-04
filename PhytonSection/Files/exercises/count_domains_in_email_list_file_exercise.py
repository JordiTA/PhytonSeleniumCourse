"""
Read the list of email addresses from the input file and create a dictionary
with keys being domain name and value being the number of occurrences for the domain.
In other words count how many times each domain exists and create a report of the count as a dictionary.
Save the output into a .json file.

- input file: count_domains_in_email_list_file_exercise_input.csv
- output file: count_domains_in_email_list_file_exercise_output.json

Example output:
{'yahoo.com': 19, 'gmail.com': 20, 'msn.com': 16, 'supersqa.com': 20, 'outlook.com': 25}

"""

import pdb
import json

inputFile = "count_domains_in_email_list_file_exercise_input.csv"
outputFile = "count_domains_in_email_list_file_exercise_output.json"


# # --------------------------------------------------------

def readingEmailsFromFile(filePath):
    print(f"Reading file in: {filePath}")
    with open(filePath, 'r') as file:
        content = file.readlines()

    contentClean = [i.strip(',\n') for i in content]

    return contentClean

# # --------------------------------------------------------

def countDomains(emailsList):
    print("Counting Domains")
    domainCount = {}
    for email in emailsList:
        domain = email.split('@')[-1]
    
        if domain not in domainCount.keys():
            domainCount[domain] = 1
        else:
            domainCount[domain] = domainCount[domain] + 1
    
    return domainCount

# # --------------------------------------------------------

def saveOutputFile(countsDict, jsonFilePath):
    print(f"Wrinting json File output in: {jsonFilePath}")
    with open(jsonFilePath, 'w') as file:
        jsonWrite = json.dumps(countsDict, indent=4)
        file.write(jsonWrite)

# # --------------------------------------------------------
# # Calling Functions

# READING
domainsList = readingEmailsFromFile(inputFile)
# FORMATING
domainDict = countDomains(domainsList)
# WRITING
saveOutputFile(domainDict, outputFile)