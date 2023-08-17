# import the class
# instantiate some objects - we call constructor
# call some methods on the objects

# from module account import Class Account
from account import Account

# instantiate bart's and lisa's accounts
bart_account = Account(20)
lisa_account = Account(500)

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

print(f'There are {Account.number_created} bank accounts.')


print(lisa_account)
print(bart_account)


if lisa_account:
    print('True')
else:
    print('False')

negative_account = Account(-20)
if negative_account:
    print('True')
else:
    print('False')

accounts = [lisa_account, bart_account]
for account in accounts:
    print(account)


# java style getters and setters are methods

# objects are not supported by less than comparison, so no sorting out of the box
# sorted_accounts = accounts.sort()
print(lisa_account.get_firstname())
lisa_account.set_firstname('Lisa')
bart_account.set_firstname('Bart')
print(lisa_account.get_firstname())
print(bart_account.get_firstname())


# c style properties
lisa_account.lastname = 'Simpson'
print(lisa_account.lastname)
bart_account.lastname = 'Simpson'
print(bart_account.get_firstname() + " " + bart_account.lastname)

