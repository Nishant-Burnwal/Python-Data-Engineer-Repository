# PROG 1: To use Join

def words_uppercase():
    places_list = []

    for i in range(1, 6):
        place = input(f"Enter the name of place {i}: ")
        places_list.append(place)

    print(f"\nPlaces stored in list: {places_list}")

    # create a new stirnf with all the place names eperated by comma and space

    places_str = ', '.join(places_list)

    print("Places seperated by comma and space in upper case: ", places_str.upper())

words_uppercase()