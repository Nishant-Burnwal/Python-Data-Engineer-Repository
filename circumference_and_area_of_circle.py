# Compute Circumference and Area of Circle
# Define PI
PI = 22 / 7
try:
      # Step 2: Take radius from user
      radius_inch = float(input("Enter the radius of the circle in inches: "))
except ValueError as err:
      print("You have entered a wrong radius. Error: {err}")

# Convert radius inch to cm
radius_cm = radius_inch * 2.54

# Compute circumference and area
circumference_cm = 2 * PI * radius_cm
area_square_cm = PI * (radius_cm ** 2)
volume_cube_cm = PI * (radius_cm ** 3)

# Print the radius with new line separator
print(f"\nCircumference of the Circle is {round(circumference_cm, 2)} cm and",
      f"Area of the Circle is {round(area_square_cm, 2)} sqcm",
      f"Volume of the Circle is {round(volume_cube_cm, 2)} sqcm", sep="\n")