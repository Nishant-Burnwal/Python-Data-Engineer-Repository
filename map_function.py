# PROG: 3.1 Map Fuction
# Syntax: map(func, iter) iter can be list, tuple, set etc

numbers_list = [1, 2, 3, 4, 5]
print(f"The Original list is {numbers_list}")
"""
    Map returns the map object not the list
"""
double_list = map(lambda x: x * 2, numbers_list)
print(f"Double list is {double_list}")

"""
    Map returns the map object not the list
    therefore we used list type conversion here
"""
double_list = list(map(lambda x: x * 2, numbers_list))
print(f"Double list is {double_list}")