class BankAccount:
    # Constructor to initialize account holder's name and starting balance
    def __init__(self, name, balance=0):
        self.name = name          # Account holder's name
        self.balance = balance    # Initial balance (default is ₹0)

    # Method to deposit money into the account
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f" ₹{amount} deposited successfully.")
        else:
            print(" Deposit amount must be positive.")

    # Method to withdraw money from the account
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f" ₹{amount} withdrawn successfully.")
        else:
            print(" Insufficient funds. Withdrawal failed.")

    # Method to check current balance
    def check_balance(self):
        print(f" Current balance for {self.name}: ₹{self.balance}")
        return self.balance

# Menu-driven interface
if __name__ == "__main__":
    name = input("Enter account holder's name: ")
    initial_balance = float(input("Enter initial balance: ₹"))
    account = BankAccount(name, initial_balance)

    while True:
        print("\n===== Bank Menu =====")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: ₹"))
            account.deposit(amount)

        elif choice == '2':
            amount = float(input("Enter amount to withdraw: ₹"))
            account.withdraw(amount)

        elif choice == '3':
            account.check_balance()

        elif choice == '4':
            print(" Thank you for using the BankAccount system. Goodbye!")
            break

        else:
            print(" Invalid choice. Please select a valid option.")