def calculateSum(num1: int, num2: int):
    """
    Returns the sum of two numbers
    """
    return num1 + num2


total_sum = 10
bonus = 5
calculate_total = calculateSum(total_sum, bonus)
print(f"The sum is {calculate_total} \n" +
      f"This is the f-string concatination.")