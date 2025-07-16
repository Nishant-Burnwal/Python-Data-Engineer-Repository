# PROG 1.1: By using Hard Coded List

# define function
def custom_sum(numbers_list):
    total = 0
    for num in numbers_list:
        total += num
    return total

numbers_list = [29, 45, 32, 49, 27]
print(f"The original list is {numbers_list}")

custom_result = custom_sum(numbers_list)
print(f"The Original list is {custom_result}")

bulletin_result = sum(numbers_list)

print(f"Comparing the results of function and bulletin function: {custom_result == bulletin_result}")

