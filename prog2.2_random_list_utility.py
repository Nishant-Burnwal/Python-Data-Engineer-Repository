# PROG 2.2: Prime Factor Random List Utility

# Returns a dictionary mapping each number in the list to its prime factors
def get_random_prime_factors(random_list):
    random_prime_factor_dict = {}
    for random_number in random_list:
        random_prime_factors = get_prime_factors(random_number)
        random_prime_factor_dict[random_number] = random_prime_factors
    return random_prime_factor_dict

# Returns a list of prime factors for a single number
def get_prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

# Creates a dictionary mapping each unique prime factor to the list of numbers that contain it
def get_prime_factor_random_list(random_prime_factor_dict):
    prime_random_dict = {}

    for random_number in random_prime_factor_dict:
        random_prime_factors = random_prime_factor_dict[random_number]
        unique_prime_factors = set(random_prime_factors)

        for prime_factor in unique_prime_factors:
            prime_random_list = prime_random_dict.get(prime_factor)
            if prime_random_list is None:
                prime_random_list = []
            prime_random_list.append(random_number)
            prime_random_dict[prime_factor] = prime_random_list

    return prime_random_dict
