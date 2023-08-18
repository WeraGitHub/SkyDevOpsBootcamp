# import datetime modul
from datetime import datetime
from custom_exceptions import NegativeAmountError, InsufficientFundsError

# from module account import Class Account
from account import Account

from savings_account import SavingsAccount

# instantiate bart's and lisa's accounts
bart_account = Account(20, '12-59-55', 1564589)
lisa_account = Account(500, '01-02-03', 9999999)

# call method deposit on the bart's account object
print(bart_account.get_balance())
print(lisa_account.get_balance())

bart_account.deposit(25)
lisa_account.deposit(10)
lisa_account.deposit(10)

print(bart_account.get_balance())
print(lisa_account.get_balance())

lisa_account.withdraw(30)
print(lisa_account.get_balance())

print(f'There are {Account.get_account_count()} bank accounts.')


print(lisa_account)
print(bart_account)


if lisa_account:
    print('True')
else:
    print('False')

negative_account = Account(-20, '55-55-55', 89898989)
if negative_account:
    print('True')
else:
    print('False')

accounts = [lisa_account, bart_account]
for account in accounts:
    print(account)

print(accounts)  # this is possible thanks to overriding repr method in our class


# java style getters and setters are methods

# objects are not supported by less than comparison, so no sorting out of the box
# sorted_accounts = accounts.sort()
print(lisa_account.get_firstname())
lisa_account.set_firstname('Lisa')
bart_account.set_firstname('Bart')
print(lisa_account.get_firstname())
print(bart_account.get_firstname())


# c# style properties
lisa_account.lastname = 'Simpson'
print(lisa_account.lastname)
bart_account.lastname = 'Simpson'
print(bart_account.get_firstname() + " " + bart_account.lastname)


print("\n\n")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
print('#'*50)
print('#'*50)
print("\n\n")


bob = SavingsAccount(0, '15-12-35', 56123456,  10)
print(bob)
print(bob.calculate_intrest())
bob.deposit(100)
print(bob)
print(bob.calculate_intrest())

print(bob.get_date_created())
# bob.deposit(-100)
bob.deposit(10000)

print(bob.get_balance())

# bob.withdraw(150000)
bob.withdraw(500)
print(bob.get_balance())

try:
    bob.deposit(-100)
except NegativeAmountError as err:
    print(err)
else:
    print("Deposit completed")
finally:
    print("BYE\n")

try:
    bob.deposit(500)
except NegativeAmountError as err:
    print(err)
else:
    print("Deposit completed")
finally:
    print("BYE\n")

try:
    bob.withdraw(500000)
except NegativeAmountError as err:
    print(err)
except InsufficientFundsError as err:
    print(err)
else:
    print("Withdraw completed")
finally:
    print("BYE\n")

try:
    bob.withdraw(50)
except NegativeAmountError as err:
    print(err)
except InsufficientFundsError as err:
    print(err)
else:
    print("Withdraw completed")
finally:
    print("BYE\n")






