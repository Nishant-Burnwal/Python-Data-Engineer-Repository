# PROG 2: to implement slicing

user_string = "Internship"

print(user_string)

sliced_string = user_string[:6:]

print(sliced_string)


sliced_string = user_string[6:10:]

print(sliced_string)

sliced_string = user_string[::2]

print(sliced_string)

sliced_string = user_string[::4]

print(sliced_string)

sliced_string = user_string[::-1]

print(sliced_string)


def create_new_string(input_string):
    # first character
    first_char = input_string[0]

    # Middle Character
    middle_index = len(input_string) // 2
    print(middle_index)
    middle_char = input_string[middle_index]

    # last index
    last_char = input_string[-1]

    new_string = first_char + middle_char + last_char

    return new_string

input_string = 'Knowledge'
print(len(input_string))
output_string = create_new_string(input_string)

print(f"Input String: {input_string}")
print(f"Output String contaning first middle and last character: {output_string}")
