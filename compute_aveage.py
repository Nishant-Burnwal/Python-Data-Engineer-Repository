# PROG 5: Compute Average

def compute_average(number_list):
    """
        Returns the average of the list
    """
    total = sum(number_list)
    count = len(number_list)
    avg_list = total/count
    if count == 0:
        return 0
    else:
        return avg_list

# Original List
number_list = [10, 20, 30, 40, 50]
print(f"Original List: {number_list}")

# Average List
average_list = compute_average(number_list)
print(f"Average of list is {average_list}")

