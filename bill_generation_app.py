# Constants for GST rates
APPLE_GST = 0.12  # 12% GST for Apple
ORANGE_GST = 0.05  # 5% GST for Orange
try:
# Take input from the user
    buyer_name = input("Enter Buyer Name: ")

    apple_price_kg = float(input("Enter Apple price per kg: "))
    apple_quantity_kg = float(input("Enter Apple quantity in kg: "))

    orange_price_kg = float(input("Enter Orange price per kg: "))
    orange_quantity_kg = float(input("Enter Orange quantity in kg: "))
except:
    print("You Entered an wrong user input.")

# Calculate total price (without GST)
total_price_apple = apple_price_kg * apple_quantity_kg
total_price_orange = orange_price_kg * orange_quantity_kg

# Calculate GST amounts
total_gst_apple = total_price_apple * APPLE_GST
total_gst_orange = total_price_orange * ORANGE_GST

# Calculate total billing amount (inclusive of GST)
total_billing_apple = total_price_apple + total_gst_apple
total_billing_orange = total_price_orange + total_gst_orange

# Calculate total and rounded total
total_amount = total_billing_apple + total_billing_orange
total_round_amount = round(total_amount)

# Print the bill in table format
print("\n" + "=" * 60)
print(f"Buyer Name: {buyer_name}")
print("=" * 60)
print(f"{'Item':<10} | {'Price/Unit':<12} | {'Qty(kg)':<8} | {'GST':<8} | {'Total w/ GST':<15}")
print("-" * 60)
print(f"{'Apple':<10} | Rs.{apple_price_kg:<10.2f} | {apple_quantity_kg:<8.2f} | Rs.{total_gst_apple:<8.2f} | Rs.{total_billing_apple:<15.2f}")
print(f"{'Orange':<10} | Rs.{orange_price_kg:<10.2f} | {orange_quantity_kg:<8.2f} | Rs.{total_gst_orange:<8.2f} | Rs.{total_billing_orange:<15.2f}")
print("-" * 60)
print(f"{'Total':<40} Rs.{total_amount:<15.2f}")
print(f"{'Total Rounded':<40} Rs.{total_round_amount:<15}")
print("=" * 60)
