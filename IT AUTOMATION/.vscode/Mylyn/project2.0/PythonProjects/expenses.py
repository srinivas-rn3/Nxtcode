class Expense:
    def __init__(self,amount,description,category):
        self.amount = amount 
        self.description = description 
        self.category = category 

def add_expense(expenses):
        amount = float(input("Enter the expense amount: "))
        description = input("Enter expense description: ")
        category = input("Enter expense category: ")
        expenses.append(Expense(amount,description,category))

def view_summary(expenses):
        categories = {}
        total_spending = 0 
        for expense in expenses:
            if expense.category in categories:
                categories[expense.category] += expense.amount
            else:
                categories[expense.category] = expense.amount 
            total_spending += expense.amount 
        print("\n============ Expense Summary ===========")
        for category,spending, in categories.items():
            print(f"{category}:{spending}")
        print(f"Total  Spending :{total_spending}")
        
def save_expesens(expenses,filename):
        with open(filename,'w') as file:
            for expense in expenses:
                file.write(f"{expense.amount},{expense.description},{expense.category}\n")

def load_expense(filename):
        expense = []
        try:
            with open(filename,'r') as file:
                for line in file:
                    amount,description,category = line.strip().split(',')
                    expense.append(Expense(float(amount),description,category))
        except FileNotFoundError:
            pass 
        return expense

def main():
    filename = r"C:\Users\srini\OneDrive\Documents\myexpenses_Feb_2024.txt"
    expenses = load_expense(filename)
    while True: 
        print("\n========= Expense Tracker ==========")
        print("1. Add Expense")
        print("2. View Expense")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_summary(expenses) 
        elif choice == '3':
            save_expesens(expenses,filename)
            print("Exiting program...")
            break
        else:
            print("Invalid  choice . Please try again!!")

if __name__ == '__main__':
    main()