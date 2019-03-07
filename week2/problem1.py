balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monthly_interest_rate = annualInterestRate / 12.0

for month in range(1, 13):
    minimum_monthly_payment = monthlyPaymentRate * balance
    monthly_unpaid_balance = balance - minimum_monthly_payment
    balance = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)
    # print(month, round(balance, 2))

print(round(balance, 2))
