# PROG 2.1: Generate Random List Function

import random

# Function to generate a list of random numbers based on input limits and size
def create_random_list():
    # Input for lower limit, upper limit, and number of random numbers
    lower_entered = input("Enter lower limit > 1 for random number: ")
    upper_entered = input("Enter higher limit for random number: ")
    size_entered = input("Enter total random numbers to generate: ")

    # Convert inputs to integers if valid, else set to None
    lower = int(lower_entered) if lower_entered.isdigit() else None
    upper = int(upper_entered) if upper_entered.isdigit() else None
    size = int(size_entered) if size_entered.isdigit() else None

    random_list = []

    # Check that all inputs are valid and limits make sense
    if (lower is not None and upper is not None and size is not None and
            lower > 0 and upper > lower and size > 1 and size < (upper - lower)):
        # Generate the random list
        random_list = [random.randint(lower, upper) for _ in range(size)]
    else:
        # Show message for invalid inputs
        print(f"Invalid entry: Lower Limit ({lower_entered}), Upper Limit ({upper_entered}), or Size ({size_entered}).")

    return random_list

# Run the function and display the generated list
print(create_random_list())