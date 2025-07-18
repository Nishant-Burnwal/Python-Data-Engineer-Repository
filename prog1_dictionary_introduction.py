# PROG 1.1: Add Data In Dictionary With Hard-Coded Values

def print_friend_details(friend_details):
    print("Type of friend_details:", type(friend_details))
    # Print each detail one by one using keys
    print("\nPrinting details using keys:")
    for key in friend_details:
        print(f"{key}: {friend_details[key]}")

friend_details = {'Name': 'John', 'City of Stay': 'Mumbai', 'Pincode': '400088'}

print_friend_details(friend_details)