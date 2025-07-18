def merge_dictionaries():
    # Initial dictionary with basic details
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
    
    # Merge dictionaries using update()
    merged_dict = friend_details.copy()  # Avoid modifying original dictionary
    merged_dict.update(contact_details)

    # using dictionary unpacking (**)
    merge_dict_unpacking = {**friend_details, **contact_details}
    print(merge_dict_unpacking)

    # using | operator(Python 3.9+)
    merge_dict_union = friend_details | contact_details

    # using |= operator (Python 3.9+)
    merged_dict_ior = friend_details.copy()
    merged_dict_ior |= contact_details


    print("Merge Dictionary using update: ")
    print_dict(merged_dict)

    print("Merge Dictionary using unpacking(**): ")
    print_dict(merge_dict_unpacking)

    print("Merge Dictionary using | operator: ")
    print_dict(merge_dict_union)

    print("Merge Dictionary using |= operator: ")
    print_dict(merged_dict_ior)

    


def print_dict(details_dict):
    print("Merged Dictionary:")
    for key, value in details_dict.items():
        print(f"{key}: {value}")
    
    print("\nUsing Keys Method:", details_dict.keys())
    
    print("\nUsing Values Method:", details_dict.values())
    
    print("\nUsing Items Method:", details_dict.items())

# Main execution
merge_dictionaries()