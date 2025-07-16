# PROG 3: Convert str into Date object

from datetime import datetime

# date string
date_string = "15 Jul 2025"

print("\nDate as date string: ", date_string)

print(type(date_string))

date_object = datetime.strptime(date_string, "%d %b %Y")

print("\nDate as DateTime object: ", date_object)
print(type(date_object))
