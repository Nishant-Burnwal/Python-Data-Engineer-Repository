# PROG 4: Return Multiple values

def compute_min_max(number_list):
    """
    Description: The function finds out min and max in a list
    Parameter: number list
    Return: min_number, max_number
    """
    min_number = min(number_list)
    max_number = max(number_list)
    return min_number, max_number

# take user input length of the list
length_list = int(input("Enter the no of elements in a list: "))

number_list = []

for i in range(length_list):
    ele = int(input("Enter the elements: "))
    number_list.append(ele)
# print the list
print(f"The Original list is {number_list}")

min_value, max_value = compute_min_max(number_list)
print("Minimum value in a list is: ", min_value)
print("Maximum value in a list is: ", max_value)

print()