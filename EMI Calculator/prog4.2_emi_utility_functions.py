# PROG 4.2: EMI Utility Functions

# Calculates simple interest per period for a given principal and rate of interest
def calculate_interest(principle, roi, frequency=12):
    return round(principle * roi / (frequency * 100), 2)

# Calculates the EMI for a given principal, rate of interest, and time in years
def calculate_emi(principle, roi, time):
    interest_per_month = calculate_interest(1, roi)
    months = time * 12

    emi = (principle * interest_per_month * (1 + interest_per_month) ** months /
           ((1 + interest_per_month) ** months - 1))
    return emi

# Test the EMI calculation
print(f"EMI for Principal: 1000, ROI: 10, Years: 1 is {calculate_emi(1000, 10, 1):.2f}")
