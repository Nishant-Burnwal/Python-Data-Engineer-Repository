# PROG 3.3: Get Common Elements Main Program

import random

# Generates a random list of numbers within given limits
def create_random_list():
    lower = input("Enter Lower Limit: ")
    upper = input("Enter Upper Limit: ")
    size = input("Enter Size: ")

    if lower.isdigit() and upper.isdigit() and size.isdigit():
        lower = int(lower)
        upper = int(upper)
        size = int(size)

        return [random.randint(lower, upper) for _ in range(size)]
    else:
        print("Invalid input. Enter numeric values only.")
        return []

# Finds the maximum number in a list
def get_max_number(seq_list):
    max_lambda = lambda a, b: a if a > b else b
    max_num = seq_list[0]
    for num in seq_list[1:]:
        max_num = max_lambda(max_num, num)
    return max_num

# Generates the Fibonacci sequence up to a maximum number
def get_fibonacci_sequence(max_number):
    fibonacci_sequence = [0, 1]
    next_fibonacci = 0
    while next_fibonacci <= max_number:
        next_fibonacci = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_fibonacci)

    if fibonacci_sequence[-1] > max_number and fibonacci_sequence[-2] <= max_number:
        fibonacci_sequence = fibonacci_sequence[:-1]

    return fibonacci_sequence

# Finds common numbers between the random list and the Fibonacci sequence
def get_common_sequence(random_list, fibonacci_sequence):
    common_numbers = [num for num in random_list if num in fibonacci_sequence]
    return common_numbers

random_list = create_random_list()

if len(random_list) > 0:
    max_number = get_max_number(random_list)
    fibonacci_sequence = get_fibonacci_sequence(max_number)
    common_numbers = get_common_sequence(random_list, fibonacci_sequence)

    print(f"""\nFINAL RESULT
Common Numbers: {common_numbers}
Random Numbers: {random_list}
Fibonacci Numbers: {fibonacci_sequence}
""")
else:
    print(f"Random List {random_list} is empty. Check the input limits.")
