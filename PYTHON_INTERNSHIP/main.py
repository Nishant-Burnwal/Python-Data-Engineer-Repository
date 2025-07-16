import my_calculator

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))


result_add = my_calculator.add(first_number, second_number)
print("Sum:", result_add)

result_subtract = my_calculator.subtract(first_number, second_number)
print("Differene:", result_subtract)

result_multiple = my_calculator.multiply(first_number, second_number)
print("Product:", result_multiple)

result_divide = my_calculator.divide(first_number, second_number)
print("Quotient:", result_divide)