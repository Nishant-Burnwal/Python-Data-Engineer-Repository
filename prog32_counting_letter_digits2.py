# PROG 3.2: Counting Letters, Digits, and Special Symbols in a String Using List Comprehension

def count_characters(str_check):
    """
        Description: The function count the characters using comprehension
        Parameters: String to check
        Return: no_of_alphabets, no_of_digits, no_of_special_characters
    """
    no_of_alphabets = sum(1 for char in str_check if char.isalpha())
    no_of_digits = sum(1 for char in str_check if char.isdigit())
    no_of_special_characters = len(str_check) - no_of_alphabets - no_of_digits
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