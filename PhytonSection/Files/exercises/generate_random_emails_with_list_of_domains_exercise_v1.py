"""
Exercises:
Create a file with list of randomly generated email addresses.
The email addresses must have domain name from the
given list of domains.
* Domain list is provided as variable 'list_of_domains'

HINT:
To generate random string with all lower case you can use this code
import random
import string
letters = string.ascii_lowercase
random_string = ''.join(random.choice(letters) for i in range(length))

V1:
- Create 20 emails for each domain
- Output a csv file with one email on each line and each line ending with a comma
- Output file name: out_generate-random_email_with_list_of_domains_v1.csv
"""

import pdb
import random
import string

outputPath = '.\out_generate_random_email_with_list_of_domains_v1.cvs'

list_of_domains = ['supersqa.com', 'gmail.com', 'yahoo.com', 'outlook.com', 'msn.com']

lengthEmail = 5
letters = string.ascii_lowercase

allEmails =[]

for domain in list_of_domains:
    for i in range(20):
        random_string = ''.join(random.choice(letters) for i in range(lengthEmail))
        email = random_string + '@' + domain
        allEmails.append(email)
        print(email)

with open(outputPath, 'w') as file:
    for email in allEmails:
        file.write(email + ',\n')