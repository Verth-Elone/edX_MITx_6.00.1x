
# Test values:
balance = 999999
annualInterestRate = 0.18

# Basic calculations:
monthly_interest_rate = annualInterestRate / 12.0
lower_bound = balance / 12.0
upper_bound = (balance * (1 + monthly_interest_rate)**12) / 12.0


def evaluate_payment(starting_balance: float, payment: float) -> float:
    """

    :param starting_balance:
    :param payment:
    :return:
    """
    actual_balance = starting_balance
    for month in range(1, 13):
        balance_after_payment = actual_balance - payment
        actual_interest = balance_after_payment * monthly_interest_rate
        actual_balance = balance_after_payment + actual_interest
    return actual_balance


balance_reminder = balance
mean_payment = 0.0
while abs(balance_reminder) > 0.01:
    mean_payment = (lower_bound + upper_bound) / 2
    balance_reminder = evaluate_payment(balance, mean_payment)
    if balance_reminder > 0.0:
        lower_bound = mean_payment
    elif balance_reminder < 0.0:
        upper_bound = mean_payment

print('Lowest payment: ', round(mean_payment, 2))
