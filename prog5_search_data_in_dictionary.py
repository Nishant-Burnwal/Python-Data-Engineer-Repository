# friend details dict
friend_details = {
'Friend1': [
    {'City': 'New York', 'Pincode': '100100'},
    {'Email': 'friend1@example.com', 'PhoneNumber': '9565656565'}
],
'Friend2': [
    {'City': 'Los Angeles', 'Pincode': '900900'},
    {'Email': 'friend2@example.com', 'PhoneNumber': '9876543210'}
],
'Friend3': [
    {'City': 'Chicago', 'Pincode': '606606'},
    {'Email': 'friend3@example.com', 'PhoneNumber': '9123456789'}
],
'Friend4': [
    {'City': 'Houston', 'Pincode': '770770'},
    {'Email': 'friend4@example.com', 'PhoneNumber': '9988776655'}
],
'Friend5': [
    {'City': 'Miami', 'Pincode': '331331'},
    {'Email': 'friend5@example.com', 'PhoneNumber': '9090909090'}
]
}

#function to get friend details
def get_friend_details():

    friend_name = input("Enter friend's name: (Friend1/Friend2/Friend3/Friend4/Friend5): ")
    detail_type = input("Enter detail type (City/Pincode/Email/PhoneNumber): ")
 
    if friend_name in friend_details:
        print(f"{friend_name}: {friend_details[friend_name]}")

        if detail_type in friend_details[friend_name][0] or detail_type in friend_details[friend_name][1]:
            if detail_type in friend_details[friend_name][0]:
                print(f"{friend_name}'s {detail_type}: {friend_details[friend_name][0][detail_type]}")
            else:
                print(f"{friend_name}'s {detail_type}: {friend_details[friend_name][1][detail_type]}")
        else:
            print("Invalid input type")

    else:
        print(f"{friend_name}'s name not in friend_details")

def main():
    get_friend_details()

if __name__ == "__main__":
    main()