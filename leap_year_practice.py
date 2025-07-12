def isLeapYear():
    """
        Check if the year is leap year or not.
    """
    try:
        year = int(input("Enter the year: "))
    except:
        print("You Entered a wrong value.")
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) :
        print(f"{year} is leap year.")
    else:
        print(f"{year} is not leap year.")

isLeapYear()
