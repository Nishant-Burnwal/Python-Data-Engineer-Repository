# PROG 3.2: Get Max and Common Sequence Utility

# Define a function to find the maximum number in the list
def get_max_number(seq_list) :
    # Create a lambda function to find the maximum number in the list
    max_lambda = lambda a, b: a if a > b else b

    # Find the maximum number in the list
    max_num = seq_list[0]
    for num in seq_list[1:] :
        max_num = max_lambda(max_num, num)

    # Return the maximum number
    return max_num

# Function to find the common numbers in the random list and fibonacci sequence
def get_common_sequence(random_list, fibonacci_sequence):
    # Return the common numbers
    common_numbers = [num for num in random_list if num in fibonacci_sequence]
    return common_numbers
