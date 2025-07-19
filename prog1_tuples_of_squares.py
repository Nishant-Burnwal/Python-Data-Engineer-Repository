# PROG 1: Creating a Tuple of Squares and Accessing Specific Elements

def create_square_tuple():
    """
    This function generates squares of numbers from 0 to 9,
    stores them in a tuple, and accesses specific elements from it.
    """
    # Generate the list of squares using list comprehension
    square_list = [number ** 2 for number in range(10)]
    print("The List of Square of Numbers is", square_list)

    # Convert the list to a tuple using the tuple constructor
    square_tuple = tuple(square_list)

    print("Use of index for accessing elements in tuple")
    print("3rd element:", square_tuple[2])
    print("5th element:", square_tuple[4])
    print("7th element:", square_tuple[6])

    # Slicing the first 3 elements
    print("First 3 elements:", square_tuple[:3])

# Run the function
create_square_tuple()
