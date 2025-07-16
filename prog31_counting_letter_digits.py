# PROG 3.1: Counting Letters, Digits, and Special Symbols in a String Using Explicit Loops
def count_characters(str_check):
    """
        Description: The function count the characters
        Parameters: String to check
        Return: no_of_alphabets, no_of_digits, no_of_special_characters
    """
    no_of_alphabets = 0
    no_of_digits = 0
    no_of_special_characters = 0

    for char in str_check:
        if char.isalpha():
            no_of_alphabets += 1
        elif char.isdigit():
            no_of_digits += 1
        else:
            no_of_special_characters += 1
    return no_of_alphabets, no_of_digits, no_of_special_characters

def main():
    str1 = "P@#yn26at^&i5ve"
    print(f"The Original String is: {str1}")
    no_of_alphabets, no_of_digits, no_of_special_characters = count_characters(str1)

    print(f"No. of letters: {no_of_alphabets}")
    print(f"No of digits: {no_of_digits}")
    print(f"No od special characters: {no_of_special_characters}")

if __name__ == "__main__":
    main()