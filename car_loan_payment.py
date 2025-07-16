# Program 2: Car Loan Paymet

def calculate_car_loan_payment(P, Y, R):
    """
    Compute the monthly car loan payment
    """
    r = R / 100 / 12
    n = Y * 12
    monthly_payment = (P * r  * (1 + r) ** n) / ((1 + r) ** n - 1)
    return round(monthly_payment, 2)

principal_amount = float(input("Eter the Principal amount in rupees: "))
years_to_pay_off = float(input("Enter the duration to pay off the loan in years: "))
annual_interest_rate = float(input("Enter the anual years rate in percentage: "))

monthly_payment = calculate_car_loan_payment(principal_amount, years_to_pay_off, annual_interest_rate)
print(f"Montly Car payment is:  {monthly_payment}")

