print("Electricity bill estimator")

cents_per_kwh= float(input("Cents per kWh:"))
daily_use= float(input("Daily use per kwh:"))
billing_days= int(input("Number of billing days:"))

estimated_bill= cents_per_kwh/100 * daily_use * billing_days
print(f"Your estimated bill is {estimated_bill}")