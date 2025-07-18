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
print(merge_dict)

if 'Pincode' in merge_dict:
    del merge_dict['Pincode']

print(merge_dict)