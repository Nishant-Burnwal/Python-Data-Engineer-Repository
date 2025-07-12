# Places to Visit Code

# Using help built-in function to know more about print
help(print)

# Using help built-in function to know more about input
help(input)

# Take User Inputs for Name, Places, and Year
try:
    user_name = input("Enter the user name: ")
    first_place = input("Enter the first place you would like to visit: ")
    second_place = input("Enter the second place you would like to visit: ")
    third_place = input("Enter the third place you would like to visit: ")
    year = int(input("Enter the year to visit: "))

    # Print the user and the places to visit for the year
    # Using f-string, sep, and end
    print(f"{user_name} and places to visit are:", first_place, second_place, third_place, sep=" , ", end="\n")
    print(f"In the year {year}")

except ValueError:
    print("You entered an incorrect value for the year. It must be an integer.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    print("Program compiled successfully.")
