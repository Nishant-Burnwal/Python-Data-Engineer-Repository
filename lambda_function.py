# PROG 3: Lambda Function

str_1 = "Internship"

upper = lambda text: text.upper()

print(f"The upper case of {str_1} is {upper(str_1)}")

# Greater of two numbers

max = lambda a, b: a if(a > b) else b
print(f"The Greater of two numbers is: {max(10, 13)}")