# create class Account
class Account:
    # create a variable with a value of 0
    _number_created = 0

    # create a method on a class level
    @classmethod
    def get_account_count(cls):  # declare method
        # return number of instances of Accounts
        return Account._number_created

    # initiate class with the right arguments
    def __init__(self, opening_balance, sortcode, account_number):
        # assign the arguments to it's properties
        self.__balance = opening_balance
        self._firstname = "Unknown"
        self._lastname = "Unknown lastname"
        self._sortcode = sortcode
        self._account_number = account_number
        Account._number_created += 1

    # override the __str__ method
    def __str__(self):
        return f'Bank account has a balance ${self.__balance}'

    # override the bool method
    def __bool__(self):
        # if self.__balance > 0:
        #     return True
        # else:
        #     return False
        return True if self.__balance > 0 else False

    # override represent method (to be able to see the overriden str in a collection)
    def __repr__(self):
        return self.__str__()

    # reading - getter
    def get_firstname(self):
        # return the first name string in a capitalised form
        return self._firstname.capitalize()

    # writing - setter
    def set_firstname(self, new_firstname):
        # assign new value to the firstname property
        self._firstname = new_firstname

    # get last name
    @property
    def lastname(self):
        return self._lastname

    # set last name
    @lastname.setter
    def lastname(self, new_lastname):
        self._lastname = new_lastname

    # getter to read a piece of data - account balance here
    def get_balance(self):
        return self.__balance

    # method to allow money deposits
    def deposit(self, amount):
        # validate that user is depositing a positive amount
        if amount > 0:
            self.__balance += amount
        # otherwise print warning
        else:
            print("You can't deposit that!!!!")

    # define a method to withdraw the monies
    def withdraw(self, amount):
        # check if user has enough money in the account to facilitate the withdrawal
        if self.__balance > amount:
            self.__balance -= amount
        # otherwise print warning
        else:
            print("Insufficient funds")


# encapsulation
# loose coupling
# high cohesion - putting things together that belong together.
# abstraction
# inheritance
# polymorphism
