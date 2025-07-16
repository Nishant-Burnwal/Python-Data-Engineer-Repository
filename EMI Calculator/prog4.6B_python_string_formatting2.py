# PROG 4.6B: Python String Formatting Samples

# Define a simple Person class with __init__ and __str__ methods
class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Height: {self.height} feet"


# Create a Person object
john = Person("John", 25, 5.845)

# Print the Person object using f-string (__str__ method is called)
print(f"Person Details: {john}\n")

# Print using f-string with expressions and format specifiers
print(f"Person Details with Expressions: {john.name.upper()}, {john.age + 5}, "
      f"{john.height:.1f} feet\n")

# Print using f-string with multiline text
print(f"""Person Details (Multiline):
Name: {john.name}
Age: {john.age}
Height: {john.height:.2f} feet
""")

# Print in a simple table format
print(f"{'-' * 40}")
print(f"| {'Name':<10} | {'Age':^10} | {'Height':>10} |")
print(f"{'-' * 40}")
print(f"| {john.name:<10} | {john.age:^10} | {john.height:>10.2f} |")
print(f"{'-' * 40}\n")

# Use str.format() with a template string
template_string = "Hello {first_name}, you are {age} years old and {height} feet tall."
formatted_string = template_string.format(
    first_name=john.name,
    age=john.age,
    height=round(john.height, 2)
)
print(f"Using Template String:\n{formatted_string}")
