#only use hard coding when required
PI = 22/7

def calculateArea(radius: float):
    """
    Returns Area of a Circle
    """
    return PI * radius * radius

radius_of_circle = int(input("Enter radius of the Circle: "))
area_of_circle = calculateArea(radius_of_circle)
print(f"Area of the circle: {area_of_circle}")

