# PROG: 1.2 List Creation
def create_a_list():
    """
        Create a list by taking user input
    """
    num_elemets = int(input("Enter the number of elements in the list: "))
    numbers_list = []
    for i in range(num_elemets):
        while True:
            try:
                elemet = int(input(f"Enter number {i}: "))
                numbers_list.append(elemet)
                break 
            except ValueError:
                print("Invalid input, please enter a valid number.")

    print(f"The Original Created List is: {numbers_list}")

create_a_list()