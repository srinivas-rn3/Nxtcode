class Expense:
    def __init__(self,amount,category):
        self.category = category 
        self.amount = amount 

def add_expense(expenses):
    amount = float(input("Enter the amount: "))
    category = input("Enter the category ") 
    expenses.append(Expense(amount,category))

def display_expenses(expenses):
    categories = {}
    total_spending = 0
    for expense in expenses:
        category = expense.category
        amount = expense.amount
        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount
        total_spending += amount 
    print("------------Display Expenses-------------")
    for c,a in categories.items():
        print(f"Category: {c}")
        print(f"Total Spending by category: {a}")
    print(f"Total Spending:{total_spending}")

def main():
    expenses = []
    while True:
        print("1. Add Expense")
        print("2. Display Expense")
        print("3. Exit...")
        
        choice = input("Enter the choice: ")
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            display_expenses(expenses)
            break
        else:
            print("Invalaid Input option...Try again")
if __name__=='__main__':
    main()
'''
#  expenses list look like this
expenses = [
    Expense(amount=50.0, category='Groceries'),
    Expense(amount=25.0, category='Dining Out'),
    Expense(amount=100.0, category='Utilities')
]

'''