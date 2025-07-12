def temperature_conversion():
    "Converts and prints temprature celcius to farenhite."
    try:
        celcius = int(input("Enter the temperature in Celcius: "))
    except:
        print("You entered some wrong user value.")
    farenhite = (celcius * 9/5) + 32
    print(f"The {celcius}C to farenhite conversion: {farenhite}F")

temperature_conversion()