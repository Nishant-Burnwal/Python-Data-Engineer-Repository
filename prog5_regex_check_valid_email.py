# PROG 5: To Check Email Address

import re
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.match(pattern, email):
        return True
    else:
        return False
    
email = input("Enter an email address: ")

if is_valid_email(email):
    print(f"{email} is a Vaild Email Address.")
else:
    print(f"{email} is an Invalid Email Address.")