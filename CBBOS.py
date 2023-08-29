class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False
    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            return True
        return False
    def get_balance(self):
        return self.balance
class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder):
        super().__init__(account_number, account_holder)
        self.interest_rate = 0.02
    def apply_interest(self):
        interest_amount = self.balance * self.interest_rate
        self.balance += interest_amount
class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_holder):
        super().__init__(account_number, account_holder)
        self.overdraft_limit = 1000.0
    def overdraft_protection(self):
        if self.balance < 0 and abs(self.balance) <= self.overdraft_limit:
            self.balance = 0
            return True
        return False
def main():
    accounts = {} 
    while True:
        print("\n Banking Operations")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Balance Inquiry")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            account_number = input("Enter account number: ")
            account_holder = input("Enter account holder name: ")
            account_type = input("Enter account type (Savings or Current): ").lower()
            if account_type == "savings":
                accounts[account_number] = SavingsAccount(account_number, account_holder)
            elif account_type == "current":
                accounts[account_number] = CurrentAccount(account_number, account_holder)
            else:
                print("Invalid account type.")
        elif choice == "2":
            account_number = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            if account_number in accounts and accounts[account_number].deposit(amount):
                print("Deposit successful.")
            else:
                print("Invalid account or deposit amount.")
        elif choice == "3":
            account_number = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            if account_number in accounts and accounts[account_number].withdraw(amount):
                print("Withdrawal successful.")
            else:
                print("Invalid account or insufficient balance.")
        elif choice == "4":
            account_number = input("Enter account number: ")
            if account_number in accounts:
                balance = accounts[account_number].get_balance()
                print(f"Account balance: {balance}")
            else:
                print("Invalid account.")
        elif choice == "5":
            print("Exiting the program.")
            break
if __name__ == "__main__":
    main()
