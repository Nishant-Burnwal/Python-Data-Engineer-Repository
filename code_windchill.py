import math

def windchill():
    """
        Calculates Windchill Speed based on temperature and speed
    """
    # Taking user input in month
    month_number = int(input("Enter the month number(1-12): "))
    if month_number == 1 or month_number == 11 or month_number == 12:
        temperature = int(input("Enter temperature in Farenhite: "))
        wind_speed = int(input("Enter Wind Speed (miles/hour): "))
        if (temperature > 50) and (math.abs(wind_speed)> 120 or math.abs(wind_speed) < 3):
            print("The formula is not valid if temperature is larger than 50 in absolute value or if wind speed is larger than 120 or less than 3.")
        wind_chill = 0.0
        wind_chill = 35.74 + 0.6215 * temperature - 35.75 * (wind_speed ** 0.16) + 0.4275 * temperature * (wind_speed ** 0.16)
    print(f"Windchill Value of the code is: {wind_chill:.2f}")

windchill()