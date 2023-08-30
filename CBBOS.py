class BankAccount:
    def __init__(self, account_number, account_holder):
        # Constructor to initialize a BankAccount instance.
        self.account_number = account_number  # Store the account number.
        self.account_holder = account_holder  # Store the account holder's name.
        self.balance = 0.0  # Initialize the balance to zero.

    def deposit(self, amount):
        # Method to deposit funds into the account.
        if amount > 0:  # Ensure the deposit amount is positive.
            self.balance += amount  # Increase the balance by the deposit amount.
            return True  # Return True to indicate a successful deposit.
        return False  # Return False for an invalid deposit amount.

    def withdraw(self, amount):
        # Method to withdraw funds from the account.
        if amount > 0 and self.balance >= amount:
            # Ensure the withdrawal amount is positive and within available balance.
            self.balance -= amount  # Decrease the balance by the withdrawal amount.
            return True  # Return True to indicate a successful withdrawal.
        return False  # Return False for insufficient balance or an invalid withdrawal.

    def get_balance(self):
        # Method to retrieve the current balance.
        return self.balance  # Return the current balance.

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder):
        # Constructor to initialize a SavingsAccount instance, inheriting from BankAccount.
        super().__init__(account_number, account_holder)
        self.interest_rate = 0.02  # Set the default interest rate.

    def apply_interest(self):
        # Method to apply interest to the account balance.
        interest_amount = self.balance * self.interest_rate  # Calculate interest amount.
        self.balance += interest_amount  # Add interest to the balance.

class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_holder):
        # Constructor to initialize a CurrentAccount instance, inheriting from BankAccount.
        super().__init__(account_number, account_holder)

def main():
    accounts = {}  # Dictionary to store account instances.

    while True:
        print("\n Banking Operations")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Balance Inquiry")
        print("5. Fund transfer")
        print("6. Exit")
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

        elif choice == "3":
            # Withdraw money from an existing account based on user input.
            account_number = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            if account_number in accounts:
                account = accounts[account_number]  # Get the account instance
                if account.withdraw(amount):
                    print("Withdrawal successful.")
                else:
                    print("Invalid withdrawal amount or insufficient balance.")
            else:
                print("Invalid account.")

        elif choice == "4":
            # Check and display the balance of an existing account.
            account_number = input("Enter account number: ")
            if account_number in accounts:
                balance = accounts[account_number].get_balance()
                print(f"Account balance: {balance}")
            else:
                print("Invalid account.")
        
        elif choice == "5":
            # Transfer funds between two existing accounts based on user input.
            from_account_number = input("Enter your account number: ")
            to_account_number = input("Enter recipient's account number: ")
            amount = float(input("Enter transfer amount: "))
            
            if from_account_number in accounts and to_account_number in accounts:
                from_account = accounts[from_account_number]
                to_account = accounts[to_account_number]
                
                if from_account.withdraw(amount):
                    if to_account.deposit(amount):
                        print("Transfer successful.")
                    else:
                        # Rollback the withdrawal if deposit to the recipient fails.
                        from_account.deposit(amount)
                        print("Transfer failed due to recipient's account issue.")
                else:
                    print("Transfer failed due to insufficient balance.")
            else:
                print("Invalid account(s).")

        elif choice == "6":
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()
