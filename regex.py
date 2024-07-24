import re


email_condition = "^[\w*_+]+[@]{1}+[a-z]+[.]{1}+[a-z]{2,3}$"

email = input('Enter your email ID: ')
if re.search(email_condition,email):
    print('email has the right format.')
else: 
    print('Wrong format')