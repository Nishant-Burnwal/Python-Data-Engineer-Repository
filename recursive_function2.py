# PROG 5.1: Recursive Function

def factorial(num):
    """
        Description: This function is used to find the factorial
        Parameter: It is a number for which facorial is calculated
        Return: The factorial of a number using recursion
    """
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)
    
number = int(input("Enter the numbe to find the factorial: "))

result = factorial(number)
print(f"Factorial of {number} is {result}")