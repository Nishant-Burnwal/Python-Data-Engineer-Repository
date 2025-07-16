# PROG 2.3: Prime Factors of Random List

import random

# Generates a list of random numbers within given limits
def create_random_list():
    lower = int(input("Enter lower limit > 1 for random number: "))
    upper = int(input("Enter upper limit: "))
    count = int(input("How many random numbers to generate?: "))

    random_list = []
    if lower > 1 and upper > lower and count > 0:
        for _ in range(count):
            random_list.append(random.randint(lower, upper))
    return random_list

# Returns the list of prime factors for a single number
def get_prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        if n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        else:
            divisor += 1
    return factors

# Creates a dictionary mapping each random number to its prime factors
def get_random_prime_factors(random_list):
    result = {}
    for num in random_list:
        result[num] = get_prime_factors(num)
    return result

# Currently returns the same dictionary without changes
def get_prime_factor_random_list(prime_factor_dict):
    return prime_factor_dict

# Generate random numbers
random_list = create_random_list()
print(f"Random List Generated: {random_list}")

# If the list is valid, process prime factors
if len(random_list) > 0:
    random_prime_factor_dict = get_random_prime_factors(random_list)
    prime_random_dict = get_prime_factor_random_list(random_prime_factor_dict)

    print(f"Random Numbers with Prime Factors: {random_prime_factor_dict}")
    print(f"Prime Factor to Random List Mapping: {prime_random_dict}")
else:
    print(f"Random List {random_list} is empty. Check the input limits.")
