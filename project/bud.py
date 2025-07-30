def main():
    print("budget tracker")
    income = float(input("enter the total amount"))
    expenses = {}
    while True:
        expense_name = input('enter the expenses:')
        if expense_name== 'done':
            break
        expense_amount = float(input('enter the amount of'+ expense_name +':'))
        expenses[expense_name] = expense_amount
    total_expenses = sum(expenses.values())
    surplus_or_deficit = income - total_expenses
    print("budget summary")
    print("total income: $"+str(round(income,2)))
    print("total expenses: $"+str(round(total_expenses,2)))
    print("budget breakdown")
    for name,amount in expenses.items():
        print(" "+ name +":$"+str(round(amount,2)))
    print("surplus/deficit:$"+str(round(surplus_or_deficit,2)))

if __name__ == "__main__":
    main()