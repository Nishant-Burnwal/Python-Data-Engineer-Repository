# PROG 2.1: By using slicig

#Define reverse_list function
def reverse_list(numbers):
    """
        Returns Reverse of a list
    """
    return numbers[::-1]

numbers = [29, 45, 32, 49, 37]
print(f"The original list is {numbers}")

reversed_numbers = reverse_list(numbers)
print(f"The Reversed list using slicing is {reversed_numbers}")