import threading

# Instruction 1: Printing the name of the main thread
print(f'Main or Default Thread Name is {threading.current_thread().name}')

# Instruction 2: Define a variable y and assign value 100
x = 100
y = 100

# Instruction 3: Add the variable x and y then assign the result to a new variable z
z = x + y

# Instruction 4: Display the result to stdout using print format
print(f'The Result of adding {x} and {y} is {z}')

# The result of adding two numbers is z = x + y
print(f"The result is {z}")
