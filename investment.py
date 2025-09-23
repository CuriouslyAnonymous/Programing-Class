investment_amount = int(input("Enter the investment amount: "))
while investment_amount <= 0 or investment_amount >= 50000:
    print("Your input was incorrect. Please enter a value greater than 0 but less than 50,000.")
    investment_amount = int(input("Enter the investment amount: "))

interest_rate = int(input("Enter the annual interest rate (%): "))
while interest_rate <= 0 or interest_rate >= 15:
    print("Your input was incorrect. Please enter a value greater than 0 but less than 15.")
    interest_rate = int(input("Enter the annual interest rate (%): "))

years = int(input("Enter the number of years: "))
while years <= 0:
    print("Your input was incorrect. Please enter a value greater than 0.")
    years = int(input("Enter the number of years: "))

months = years * 12
monthly_interest_rate = (interest_rate / 12) / 100
total_amount = 0

for month in range(1, months + 1):
    total_amount += investment_amount
    interest = round(total_amount * monthly_interest_rate, 2)
    total_amount += interest
    if month % 12 == 0:
        year = month // 12
        print(f"Year {year}: ${round(total_amount, 2)}")

print("\nFinal Investment Calculation")
print(f"Investment Duration: {years} years")
print(f"Annual Interest Rate: {interest_rate}%")
print(f"Monthly Investment Amount: ${round(investment_amount, 2)}")
print(f"Total Investment After Compounding: ${round(total_amount, 2)}")

print("\nCompleted by, Aldo Dillard Jefferson")







