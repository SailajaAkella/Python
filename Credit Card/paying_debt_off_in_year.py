balance = 3926
annualInterestRate = 0.2
monthlyInterestRate = (annualInterestRate) / 12.0

minimumFixedMonthlyPayment = 10

def get12MonthBalance():
    updatedBalanceEachMonth = balance
    for i in range(0, 12):
        monthlyUnpaidBalance = updatedBalanceEachMonth - minimumFixedMonthlyPayment
        updatedBalanceEachMonth = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance) 
    return updatedBalanceEachMonth


while(get12MonthBalance() > 0):
    minimumFixedMonthlyPayment+=10

print('Lowest Payment:', minimumFixedMonthlyPayment)