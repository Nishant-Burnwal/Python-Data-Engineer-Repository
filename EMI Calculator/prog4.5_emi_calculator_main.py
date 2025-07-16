# PROG 4.5: EMI Calculator Main

# Calculate monthly interest for given principal and annual rate
def calculate_interest(principal, roi, frequency=12):
    return round(principal * roi / (frequency * 100), 2)

# Calculate EMI for given principal, annual rate and time in years
def calculate_emi(principal, roi, time):
    interest_per_month = calculate_interest(1, roi)
    months = time * 12
    emi = (principal * interest_per_month * (1 + interest_per_month) ** months /
           ((1 + interest_per_month) ** months - 1))
    return emi

# Generate month-wise EMI schedule as a list of dictionaries
def compute_emi_details(principal, roi, time):
    emi_details = []
    emi = calculate_emi(principal, roi, time)
    balance = principal

    for month in range(1, time * 12 + 1):
        interest = calculate_interest(balance, roi)
        principal_paid = emi - interest
        balance -= principal_paid

        if balance < 0:
            principal_paid = round(principal_paid + balance, 2)
            emi = round(principal_paid + interest, 2)
            balance = 0

        emi_details.append({
            "Month": month,
            "EMI": round(emi, 2),
            "Interest": round(interest, 2),
            "Principal": round(principal_paid, 2),
            "Balance": round(balance, 2)
        })

    return emi_details

# Display EMI details in tabular format
def display_emi_details(emi_details):
    print(f"{'-' * 65}")
    print(f"{'Month':^8} | {'EMI':^10} | {'Interest':^10} "
          f"| {'Principal':^10} | {'Balance':^10} |")
    print(f"{'-' * 65}")

    total_emi = total_interest = total_principal = 0.0

    for emi_dict in emi_details:
        month = emi_dict["Month"]
        emi = emi_dict["EMI"]
        interest = emi_dict["Interest"]
        principal_paid = emi_dict["Principal"]
        balance = emi_dict["Balance"]

        total_emi += emi
        total_interest += interest
        total_principal += principal_paid

        print(f"{month:^8} | {emi:^10} | {interest:^10} "
              f"| {principal_paid:^10} | {balance:^10} |")

    print(f"{'-' * 65}")
    print(f"{'Total':^8} | {total_emi:^10.2f} | {total_interest:^10.2f} "
          f"| {total_principal:^10.2f} | {balance:^10.2f} |")
    print(f"{'-' * 65}")

# Main program: Take input, validate and display results
principal_entered = input("Enter the Principal Amount: ")
roi_entered = input("Enter the Rate of Interest: ")
years_entered = input("Enter the Time in years: ")

principal = principal_entered.isdigit() and int(principal_entered) or None
roi = roi_entered.isdigit() and float(roi_entered) or None
years = years_entered.isdigit() and int(years_entered) or None

if principal and roi and years and principal > 0 and roi > 0 and years > 0:
    emi_details = compute_emi_details(principal, roi, years)
    display_emi_details(emi_details)
else:
    print(f"Invalid Input: {principal_entered}, {roi_entered}, {years_entered} are not valid numbers.")
