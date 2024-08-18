class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.balance = float(initial_balance)  # Ensure balance is a float
        
class User:
    def __init__(self, name):
        self.name = name
        self.accounts = []
        
    def create_account(self, account_number, initial_balance=0):
        new_account = BankAccount(account_number, float(initial_balance))  # Ensure initial balance is a float
        self.accounts.append(new_account)
        print(f"Account {account_number} created for user {self.name}")
        
    def withdraw_amount(self, account_number, amount):
        amount = float(amount)  # Convert amount to float
        for account in self.accounts:
            if account.account_number == account_number:
                if amount > account.balance:
                    print(f"Insufficient balance to withdraw ${amount}. Current balance: ${account.balance}")
                else:
                    account.balance -= amount
                    print(f"Amount ${amount} was withdrawn from account number: {account_number}. Current balance: ${account.balance}")
                return
        print(f"Account {account_number} not found.")
