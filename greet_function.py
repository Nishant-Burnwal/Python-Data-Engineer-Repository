# PROG 1.1: Take the user input

def greet_friend(name):
    """
    Greet a friend by their name
    """
    print(f"Hello, {name}! How are you today?")

name = input("Enter your friend name: ")
greet_friend(name)