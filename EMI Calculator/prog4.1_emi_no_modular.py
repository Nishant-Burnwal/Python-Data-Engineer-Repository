# PROG 4.1: EMI Calculator (Non-Modular Version)

# Input for principal amount, rate of interest, and time in years
principle_entered = input("Enter the Principal Amount: ")
roi_entered = input("Enter the Rate of Interest: ")
years_entered = input("Enter the Time in years: ")

# Validate input and convert to numbers if valid
principle = int(principle_entered) if principle_entered.isdigit() else None
roi = float(roi_entered) if roi_entered.isdigit() else None
years = int(years_entered) if years_entered.isdigit() else None

# Check if input is valid and calculate EMI if so
if (principle is not None and roi is not None and years is not None and 
    principle > 0 and roi > 0 and years > 0):

    # Calculate monthly interest rate
    interest_per_month = round(roi / (12 * 100), 2)

    # Calculate total number of months
    months = years * 12

    # Calculate EMI using the standard formula
    emi = round(principle * interest_per_month * (1 + interest_per_month) ** months /
                ((1 + interest_per_month) ** months - 1), 2)

    balance = principle

    # Print table header
    print("-" * 65)
    print(f"{'Month':^8} | {'EMI':^10} | {'Interest':^10} | "
          f"{'Principal':^10} | {'Balance':^10} |")

    total_month = total_emi = total_interest = total_principal = 0.0

    # Loop over each month to calculate payment details
    for month in range(1, months + 1):
        interest = round(balance * roi / (12 * 100), 2)
        principal = round(emi - interest, 2)
        balance = round(balance - principal, 2)

        # Adjust for final balance if it goes negative
        if balance < 0:
            principal = round(principal + balance, 2)
            emi = round(principal + interest, 2)
            balance = 0

        total_month += 1
        total_emi += emi
        total_interest += interest
        total_principal += principal

        # Print monthly details
        print(f"{month:^8} | {emi:^10} | {interest:^10} | {principal:^10} | {balance:^10}")

    # Print table footer with totals
    print("-" * 65)
    print(f"{'Total':^8} | {total_emi:^10.2f} | {total_interest:^10.2f} | "
          f"{total_principal:^10.2f} | {balance:^10.2f} |")
    print("-" * 65)

else:
    print(f"Invalid input: {principle_entered}, {roi_entered}, {years_entered} are not valid numbers.")
