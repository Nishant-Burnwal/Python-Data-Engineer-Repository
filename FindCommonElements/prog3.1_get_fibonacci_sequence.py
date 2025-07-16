# PROG 3.1: Get Fibonacci Sequence

# Returns the Fibonacci sequence up to a maximum number
def get_fibonacci_sequence(max_number):
    fibonacci_sequence = [0, 1]

    next_fibonacci = 0
    while next_fibonacci <= max_number:
        next_fibonacci = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_fibonacci)

    # Remove the last number if it exceeds the maximum
    if fibonacci_sequence[-1] > max_number and fibonacci_sequence[-2] <= max_number:
        fibonacci_sequence = fibonacci_sequence[:-1]

    return fibonacci_sequence

print("The Fibonacci sequence up to 100 is:", get_fibonacci_sequence(100))
