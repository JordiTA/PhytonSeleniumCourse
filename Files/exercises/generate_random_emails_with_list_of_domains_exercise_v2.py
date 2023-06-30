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

V2:
- Create 100 total emails with domains randomly elected from the list. So the number of emails
for each domain will be unknown.
- Output a csv file with one email on each line and each line ending with a comma
- Output file name: out_generate_random_email_with_list_of_domains_v2.csv

** the difference from V1 is the domains are random for this one.
"""

import pdb
import random
import string

outputPath = '.\out_generate_random_email_with_list_of_domains_v2.csv'

list_of_domains = ['supersqa.com', 'gmail.com', 'yahoo.com', 'outlook.com', 'msn.com']

length = 5
letters = string.ascii_lowercase

allEmails = []

for i in range(100):
    randomString = ''.join(random.choice(letters) for i in range(length))
    randomDomain = ''.join(random.choice(list_of_domains))
    email = randomString + '@' + randomDomain
    allEmails.append(email)

with open(outputPath, 'w') as file:
    for email in allEmails:
        file.write(email + ',\n')