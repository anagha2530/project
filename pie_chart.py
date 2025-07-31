import matplotlib.pyplot as plt
def main():
    expenses = {}
    while True:
        expenses_name = input("enter the name of the expense: ")
        if expenses_name == 'done':
            break
        expense_amount = input("enter the expense amount: ")
        expenses[expenses_name] = expense_amount
    plot_expenses(expenses)

def plot_expenses(expenses):
    labels = list(expenses.keys())
    values = list(expenses.values())

    plt.figure(figsize=(10,7))
    plt.pie(values, labels = labels, autopct="%1.1f%%",startangle=140)
    plt.axis("equal")
    plt.title("pie chart")
    plt.show()

if __name__ == "__main__":
    main()