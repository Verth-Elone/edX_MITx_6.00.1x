balance = 4773
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monthly_interest_rate = annualInterestRate / 12.0

minimum_fixed_monthly_payment = (balance // 120.0) * 10
# print(minimum_fixed_monthly_payment)

term_end_balance = balance
while term_end_balance > 0:
    term_end_balance = balance
    current_balance = term_end_balance
    minimum_fixed_monthly_payment += 10.0
    for month in range(1, 13):
        monthly_unpaid_balance = current_balance - minimum_fixed_monthly_payment
        current_balance = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)
        # print(month, current_balance)
    term_end_balance = current_balance

print('Lowest Payment:', minimum_fixed_monthly_payment)
# print(round(balance, 2))
