# PROG Time Conversion
try:
    # Take input for time duration in total seconds
    total_seconds = int(input("Enter the time duration in seconds: "))

    # Convert seconds to hours, minutes, and seconds
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    # Print the converted time duration
    print(
        f"\nTime duration of {total_seconds} seconds in HH:MM:SS format is "
        f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    )
except:
    print("You Entered Some Wrong User Input as text.")
finally:
    print("Time Conversion Code Compiled Successfully.")