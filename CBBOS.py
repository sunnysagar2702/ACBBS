class BankAccount:
    def __init__(self, account_number, account_holder):
        # Initialize a BankAccount instance with an account number, account holder's name, and initial balance.
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        # Deposit the given amount into the account's balance, if the amount is positive.
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        # Withdraw the given amount from the account's balance, if the amount is positive and sufficient funds are available.
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        # Return the current balance of the account.
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder):
        # Initialize a SavingsAccount instance, inheriting from BankAccount, and set a default interest rate.
        super().__init__(account_number, account_holder)
        self.interest_rate = 0.02

    def apply_interest(self):
        # Apply interest to the account's balance based on the interest rate.
        interest_amount = self.balance * self.interest_rate
        self.balance += interest_amount

class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_holder):
        # Initialize a CurrentAccount instance, inheriting from BankAccount, and set an overdraft limit.
        super().__init__(account_number, account_holder)
        self.overdraft_limit = 1000.0

    def overdraft_protection(self):
        # Apply overdraft protection by setting balance to 0 if it's negative and within the overdraft limit.
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
            # Create a new account based on user input and add it to the accounts dictionary.
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
            # Deposit money into an existing account based on user input.
            account_number = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            if account_number in accounts and accounts[account_number].deposit(amount):
                print("Deposit successful.")
            else:
                print("Invalid account or deposit amount.")

        # Other menu options (3, 4, and 5) can be similarly commented.

if __name__ == "__main__":
    main()
