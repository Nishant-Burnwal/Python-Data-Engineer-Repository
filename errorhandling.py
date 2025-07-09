try: 
    total_sum = int(input("Enter a number: "))
    bonus_points = int(input("Enter a bonus points: "))
    total = total_sum + bonus_points
    print(f"Total: {total}")
except ValueError as err:
    print(f"You entered an {err} insted of a number.")
except:
    print(f"Try again and Enter a proper Value.")