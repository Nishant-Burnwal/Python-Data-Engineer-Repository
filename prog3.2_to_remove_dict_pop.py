friend_details = {
    'Name': 'John Doe',
    'City of Stay': 'Mumbai',
    'Pincode': '400088'
}

# Additional dictionary with email and phone number
contact_details = {
    'Email': 'john.doe@example.com',
    'Phone': '1234567890'
}

# using dictionary unpacking (**)
merge_dict = {**friend_details, **contact_details}
print("The original dictionary is: ")
print(merge_dict)

print("The dictionary after using pop('Pincode') is: ")
merge_dict.pop('Pincode')

print(merge_dict)