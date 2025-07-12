# Define some constants and create our vowel list and dictionary
DEFAULT_CHAR = 'X' 
VOWEL_STRING = "AEIOU"  
VOWELS = list(VOWEL_STRING)  

# Create a dictionary where each vowel is a key and the value is the word 'Vowel'
VOWEL_DICT = dict.fromkeys(VOWELS, 'Vowel')

# Show the types and contents to the user
print(f"VOWELS List Type: {type(VOWELS)}")
print(f"VOWELS Dict Type: {type(VOWEL_DICT)}")
print(f"VOWELS List: {VOWELS}")
print(f"VOWELS Dict: {VOWEL_DICT}")

try: 
# Ask the user to enter a single character
    user_input = input("Enter a single character (A-Z): ")
except Exception as e:
    print("You Entered some wrong user input. Error: {e}")

# If the input length is not exactly 1, use DEFAULT_CHAR, else take first character and capitalize it
if len(user_input) != 1:
    char = DEFAULT_CHAR
else:
    char = user_input[0].upper()

# If the character is not a letter, switch to DEFAULT_CHAR
if not char.isalpha():
    char = DEFAULT_CHAR

# Check if the character is a vowel by looking in the list
if char in VOWELS:
    result = "Vowel"
else:
    result = "Consonant"
print(f"OPTION 1: The character '{char}' is a {result}.")

# Check if the character is a vowel by looking it up in the dictionary
result = VOWEL_DICT.get(char, 'Consonant')
print(f"OPTION 2: The character '{char}' is a {result}.")
