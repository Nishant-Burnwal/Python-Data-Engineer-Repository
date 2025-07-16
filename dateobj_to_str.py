# PROG 3.1: Convert DateObject into String

from datetime import datetime

# date string
date_string = "15 Jul 2025"

print("\nDate as date string: ", date_string)

print(type(date_string))

date_object = datetime.strptime(date_string, "%d %b %Y")

# print the datetime object
print("\nDate as DateTime object: ", date_object)
print(type(date_object))


date_string_back = date_object.strftime("%d %b %Y")

# print the date string
print("\nDate back to as Date String: ", date_string_back)
print(type(date_string_back))