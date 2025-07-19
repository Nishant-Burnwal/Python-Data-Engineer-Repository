# Traditional swapping using a third variable
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

print("\nInitial Value of a & b are")
print("a =", a)
print("b =", b)

# Swapping logic
temp = a
a = b
b = temp

print("After traditional swapping:")
print("a =", a)
print("b =", b)
