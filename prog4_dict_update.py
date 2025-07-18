def add_default_value():

    friend_details = {
    'Name': 'John Doe',
    'City of Stay': 'Mumbai',
    'Pincode': '400088'
    }

    # Dictionary before adding default Country
    print(f"Dictionary before adding Default County: {friend_details}")

    # Dictionary after adding default Country 'India'
    friend_details.setdefault('Country', 'India')
    print(f"Dictionary after adding Default County 'India': {friend_details}")

    # adding 'friend_type_list'
    friend_type_list = ['School', 'College', 'Neighbourhood']

    for i, value in enumerate(friend_type_list, start=1):
        print(f"{i}. {value}")

    try:
        choice = int(input("Enter the choice of your frined-type from the options(1-3): "))

        if 1 <= choice <= len(friend_type_list):
            friend_details['Friend-Type'] = friend_type_list[choice - 1]
        else:
            print("You have enter an number out of range(1-3).")
    
    except ValueError:
        print("Error: You have entered a number out of range(1-3). Therefore, Friend-Type dict not created")
            

    # adding friend-type from asking user
    print("Dictionary after adding friend details: ")
    print(friend_details)


add_default_value()

    
