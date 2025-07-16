# PROG 1.2: Prime Factor Main Program

# Input number to find its prime factors
number_entered = input("Enter a number > 1 to get the prime factors: ")

# Convert input to integer if valid; otherwise, set to None
number = int(number_entered) if number_entered.isdecimal() or number_entered.isdigit() else None

# Function to find prime factors of a number
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

# Check validity and display prime factors
if number is not None and number > 1:
    print(f"Prime Factors of {number}: {get_prime_factors(number)}")
else:
    print(f"Invalid number: {number_entered}. Enter a number greater than 1.")
