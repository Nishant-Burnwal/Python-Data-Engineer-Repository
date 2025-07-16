# PROG 4.3: Compute EMI Details

# Calculates simple interest per period for a given principal and rate of interest
def calculate_interest(principal, roi, frequency=12):
    return round(principal * roi / (frequency * 100), 2)

# Calculates the EMI for a given principal, rate of interest, and time in years
def calculate_emi(principal, roi, time):
    interest_per_month = calculate_interest(1, roi)
    months = time * 12

    emi = (principal * interest_per_month * (1 + interest_per_month) ** months /
           ((1 + interest_per_month) ** months - 1))
    return emi

# Computes the full EMI schedule for the given principal, ROI, and time in years
# Returns a list of dictionaries with month-wise EMI details
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

        emi_dict = {
            "Month": month,
            "EMI": round(emi, 2),
            "Interest": round(interest, 2),
            "Principal": round(principal_paid, 2),
            "Balance": round(balance, 2)
        }

        emi_details.append(emi_dict)

    return emi_details

# Example usage: compute EMI details and display as formatted output and JSON
emi_details = compute_emi_details(10000, 10, 1)
print(f"EMI Details for Principal: 10000, ROI: 10%, Years: 1")
for detail in emi_details:
    print(detail)

import json
emi_details_json = json.dumps(emi_details, indent=2)
print("JSON Payload:", emi_details_json, sep='\n')
