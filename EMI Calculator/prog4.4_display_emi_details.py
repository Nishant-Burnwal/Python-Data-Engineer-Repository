# PROG 4.4: Display EMI Details

# Calculate interest for a given principal, rate of interest and frequency
def calculate_interest(principal, roi, frequency=12):
    return round(principal * roi / (frequency * 100), 2)

# Calculate EMI for a given principal, rate of interest and time in years
def calculate_emi(principal, roi, time):
    interest_per_month = calculate_interest(1, roi)
    months = time * 12
    emi = (principal * interest_per_month * (1 + interest_per_month) ** months /
           ((1 + interest_per_month) ** months - 1))
    return emi

# Generate detailed EMI schedule with month-wise principal, interest and balance
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

# Display EMI schedule in a formatted table
def display_emi_details(emi_details):
    print(f"{'-' * 65}")
    print(f"{'Month':^8} | {'EMI':^10} | {'Interest':^10} | "
          f"{'Principal':^10} | {'Balance':^10} |")
    print(f"{'-' * 65}")

    total_month = total_emi = total_interest = total_principal = 0.0

    for emi_dict in emi_details:
        month = emi_dict["Month"]
        emi = emi_dict["EMI"]
        interest = emi_dict["Interest"]
        principal_paid = emi_dict["Principal"]
        balance = emi_dict["Balance"]

        total_month += 1
        total_emi += emi
        total_interest += interest
        total_principal += principal_paid

        print(f"{month:^8} | {emi:^10} | {interest:^10} | "
              f"{principal_paid:^10} | {balance:^10} |")

    print(f"{'-' * 65}")
    print(f"{'Total':^8} | {total_emi:^10.2f} | {total_interest:^10.2f} | "
          f"{total_principal:^10.2f} | {balance:^10.2f} |")
    print(f"{'-' * 65}")

# Example test call
display_emi_details(compute_emi_details(10000, 10, 1))
