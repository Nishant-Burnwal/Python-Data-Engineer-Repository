# PROG 4: To Use Regex To Search Digits
import re
def search_digits(s):
    pattern = r'\d'

    digits = re.findall(pattern, s)
    return digits

input_string = input("Enter s Strring: ")
digits_found = search_digits(input_string)

if digits_found:
    print(f"Digits found in the string: {digits_found}")
else:
    print("No digits found in the string.")