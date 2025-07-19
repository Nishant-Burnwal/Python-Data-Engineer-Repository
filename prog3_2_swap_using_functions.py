def swap_values(x, y):
    """Swaps two values and returns them."""
    return y, x

# Input
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

print("\nInitial Value of a & b are")
print("a =", a)
print("b =", b)

# Function call
x, y = swap_values(a, b)

print("\nAfter swapping (using function):")
print("x =", x)
print("y =", y)
