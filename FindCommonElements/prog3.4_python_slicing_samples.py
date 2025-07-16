# PROG 3.4: Python Slicing Samples

def slicing_sample():
    sample_list = list(range(10))
    print("Original List:", sample_list)

    print("Option 1:", sample_list[:])

    print("Option 2:", sample_list[0:len(sample_list)])

    print("Option 3:", sample_list[-len(sample_list):])

    print("Option 4: Last one Item:", sample_list[-1])
    print("Option 4: Last three Items:", sample_list[-3:])

    print("Option 5: All Even Numbers:", sample_list[0::2])

    print("Option 6: All Odd Numbers:", sample_list[1::2])

    # Get all Items reverse
    print("Option 7: Reverse List:", sample_list[::-1])

    # Get all except the last
    print("Option 8: All except the last:", sample_list[:-1])

    # Get all except the first
    print("Option 9: All except the first:", sample_list[1:])

    # Get all except the first and last
    print("Option 10: All except the first and last:", sample_list[1:-1])

    # Get all except the first and last 3
    print("Option 11: All except the first and last 3:", sample_list[1:-3])

    # Get all except the first 3 and last 3
    print("Option 12: All except the first 3 and last 3:", sample_list[3:-3])

    for item in sample_list:
        if item is None:
            break
    else:
        # Executed if loop didn't break
        print("All Items have Value")

slicing_sample()
