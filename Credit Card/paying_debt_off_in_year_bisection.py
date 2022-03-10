# balance = 999999
# # balance = 42
# annualInterestRate = 0.18

balance = 320000
annualInterestRate = .2

# monthlyInterestRate = (annualInterestRate) / 12.0
# monthlyPaymentLowerBound = balance / 12
# monthlyPaymentUpperBound = (balance * (1 + monthlyInterestRate) ** 12) / 12.0

# print("monthlyPaymentLowerBound: ", monthlyPaymentLowerBound)
# print("monthlyPaymentUpperBound: ", monthlyPaymentUpperBound)

# def getBalance(lower, upper):
#     minFixedMonthlyPayment = (lower + upper) / 2
#     updatedBalanceEachMonth = balance
#     for i in range(0, 12):
#         monthlyUnpaidBalance = updatedBalanceEachMonth - minFixedMonthlyPayment
#         updatedBalanceEachMonth = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
#     bal = updatedBalanceEachMonth
#     return bal, minFixedMonthlyPayment

# bal, minFixedMonthlyPayment = getBalance(monthlyPaymentLowerBound, monthlyPaymentUpperBound)

# while(abs(bal) >= 0.1):
#     if(bal < 0):
#         monthlyPaymentUpperBound = (monthlyPaymentLowerBound + monthlyPaymentUpperBound) / 2
#     else:
#         monthlyPaymentLowerBound = (monthlyPaymentLowerBound + monthlyPaymentUpperBound) / 2
#     bal, minFixedMonthlyPayment = getBalance(monthlyPaymentLowerBound, monthlyPaymentUpperBound)

# print('Lowest Payment: ', round(minFixedMonthlyPayment, 2))


monthlyInterestRate = (annualInterestRate) / 12.0
monthlyPaymentLowerBound = balance / 12
monthlyPaymentUpperBound = (balance * (1 + monthlyInterestRate) ** 12) / 12.0

def getBalance(lower, upper):
    minFixedMonthlyPayment = (lower + upper) / 2
    updatedBalanceEachMonth = balance
    for i in range(0, 12):
        monthlyUnpaidBalance = updatedBalanceEachMonth - minFixedMonthlyPayment
        updatedBalanceEachMonth = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
    return updatedBalanceEachMonth, minFixedMonthlyPayment

bal, minFixedMonthlyPayment = getBalance(monthlyPaymentLowerBound, monthlyPaymentUpperBound)

while(abs(bal) >= 0.1):
    if(bal < 0):
        monthlyPaymentUpperBound = (monthlyPaymentLowerBound + monthlyPaymentUpperBound) / 2
    else:
        monthlyPaymentLowerBound = (monthlyPaymentLowerBound + monthlyPaymentUpperBound) / 2
    bal, minFixedMonthlyPayment = getBalance(monthlyPaymentLowerBound, monthlyPaymentUpperBound)

print('Lowest Payment: ', round(minFixedMonthlyPayment, 2))
