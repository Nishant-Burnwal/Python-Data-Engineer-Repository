# PROG 2: DateTime Module

import datetime
current_datetime = datetime.datetime.now()
print("Current Date and Time is: ", current_datetime)

print("Formatted Date and Time:")

print("Month as full name: ", current_datetime.strftime("%B"))
print("Weekday as full name: ", current_datetime.strftime("%A"))
print("Year as (4 digits): ", current_datetime.strftime("%Y"))
print("Month as abbreviated name: ", current_datetime.strftime("%b"))
print("Weekday as abbreviated name: ", current_datetime.strftime("%b"))
print("Year as (two digits): ", current_datetime.strftime("%b"))
print("Day of the month(1 - 31): ", current_datetime.strftime("%d"))
print("Hour (24-Hour clock): ", current_datetime.strftime("%H"))
print("Hour (12-Hour clock): ", current_datetime.strftime("%I"))
print("Minute (00-59): ", current_datetime.strftime("%M"))
print("Seconds (00-59): ", current_datetime.strftime("%S"))
print("AM/PM indicator: ", current_datetime.strftime("%p"))




