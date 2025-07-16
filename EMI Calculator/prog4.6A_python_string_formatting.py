# PROG 4.6A: Python String Formatting Samples

# Define some sample variables
name = "John"
age = 25
height = 5.845

# Format a simple string using f-string
formatted_string = f"Name: {name}, Age: {age}, Height: {height}"
print(f"Simple Formatted String:\n{formatted_string}\n")

# Format using f-string with expressions and methods
formatted_string = f"Name: {name.upper()}, Age: {age + 5}, Height: {round(height, 2)} feet"
print(f"Formatted String with Expressions:\n{formatted_string}\n")

# Format floating-point number to 2 decimal places
formatted_string = f"Name: {name}, Age: {age}, Height: {height:.2f} feet tall"
print(f"Formatted String with Float Formatting:\n{formatted_string}\n")

# Use f-string with dictionary values
person = {"name": name, "age": age, "height": height}
formatted_string = f"Name: {person['name']}, Age: {person['age']}, Height: {person['height']}"
print(f"Formatted String with Dictionary:\n{formatted_string}\n")

# Use string method with f-string
print(f"Formatted String with Title Method:\n{formatted_string.title()}\n")

# Use str.format() method with a template string
template_string = (
    "Hello, My name is {first_name}, I am {age} years old "
    "and {height:.2f} feet tall."
)
print(template_string.format(
    first_name=person["name"],
    age=person["age"],
    height=person["height"]
), "\n")

# Use f-string with multiple lines
print(f"""Person Details:
Name: {person['name']},
Age: {person['age']},
Height: {person['height']:.2f} feet
""")
