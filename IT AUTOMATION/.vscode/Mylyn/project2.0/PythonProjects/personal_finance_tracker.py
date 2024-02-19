class Transaction:
    def __init__(self,amount,category,date,description):
        self.amount = amount 
        self.category = category 
        self.date  = date 
        self.description = description 
        
class FinanceTracker:
    def __init__(self):
        self.transactions = []
        
    def add_tranaction(self,amount,category,date,description):
        transaction = Transaction(amount,category,date,description)
        self.transactions.append(transaction)
        print("Transaction added successfully")
        
    def summary(self):
        total_income = sum(transaction.amount for transaction in self.transactions if transaction.amount > 0)
        total_expenses = sum(transaction.amount for transaction in self.transactions if transaction.amount < 0)
        net_income = total_income  - total_expenses
        print(f"Total Income : ${total_income}")
        print(f"Total Expense : ${total_expenses}")
        print(f"Net Income : ${net_income}")
        
def main():
    fin_tracker = FinanceTracker()
    while True:
        print("\nMenu")
        print("1. Add Transaction")
        print("2. Summary")
        print("3. Exit")
        choice = input("Enter the choice: ")
        if choice == '1':
            amount = float(input("Enter the amount: "))
            category = input("Enter the category: ")
            date = input("Enter the date(YYYY-MM-DD): ")
            description = input("Enter the description : ")
            fin_tracker.add_tranaction(amount,category,date,description)
        elif choice == '2':
            fin_tracker.summary()
        elif choice == '3':
            print("Exiting program...")
            break 
        else:
            print("Invalid Entry....please try again.")

if __name__ == '__main__':
    main()