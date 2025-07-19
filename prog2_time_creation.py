import sys
import timeit

# Why list take more bytes space than tuple?
# Ans. Because list are mutable and tuple are immutable therefore
# Overhead of Dynamic Allocation
# A list over-allocates memory to allow efficient appends.

# This over-allocation reduces the frequency of memory reallocations, but increases the total memory used.

# For example, a list with 3 items might reserve space for 6 items.


# Define data
numbers = list(range(10))
numbers_tuple = tuple(numbers)

# Size comparison using sys.getsizeof
print("Size of tuple:", sys.getsizeof(numbers_tuple), "bytes")
print("Size of list:", sys.getsizeof(numbers), "bytes")

# Creation time using timeit.timeit
tuple_creation_time = timeit.timeit(lambda: tuple(range(10)), number=1000000)
list_creation_time = timeit.timeit(lambda: list(range(10)), number=1000000)

print("Creation time for tuple (in seconds):", tuple_creation_time)
print("Creation time for list (in seconds):", list_creation_time)
