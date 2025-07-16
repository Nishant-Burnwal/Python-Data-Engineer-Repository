# PROG 5: Recursive Function

def factorial(num):
    """
        Returns the factorial of a number
    """
    if num == 0:
        return 1
    else:
        result = 1
        for i in range(1, num + 1):
            result *= i
        return result
    
number = int(input("Enter the numbe to find the factorial: "))

result = factorial(number)
print(f"Factorial of {number} is {result}")