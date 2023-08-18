# import class Account from module account
from account import Account
# import module datetime needed for handling dates
import datetime


# create class SavingsAccount BASED on class Account
class SavingsAccount(Account):
    # initiate class with the right arguments
    def __init__(self, opening_balance, sort_code, account_number, intrest):
        # call the initiator from the base class with it's arguments
        super().__init__(opening_balance, sort_code, account_number)
        #
        self._date_created = datetime.date.today()
        self._intrest = intrest

    def __str__(self):
        return f'Bank account is a savings account and has a balance of ${self.get_balance()}'

    def get_date_created(self):
        return self._date_created

    def get_intrest(self):
        return self.get_intrest()

    def set_intrest(self, new_intrest):
        self._intrest = new_intrest

    def calculate_intrest(self):
        return self.get_balance() * self._intrest / 100

