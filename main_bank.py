from bank_script import User, BankAccount

name = input(f"Enter your Bank Account Name: ")
account = input(f"Enter your Bank Account Number: ")
to_deposit = input(f"Enter the amount you want to deposit: ")
user = User(name)
user.create_account(account, to_deposit)

to_withdraw = input(f"Enter the amount you want to withdraw: ")
user.withdraw_amount(account, float(to_withdraw))