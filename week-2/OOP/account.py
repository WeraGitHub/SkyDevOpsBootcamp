class Account:
    _number_created = 0

    @classmethod
    def get_account_count(cls):
        return Account._number_created

    def __init__(self, opening_balance):
        self.__balance = opening_balance
        self._firstname = "Unknown"
        self._lastname = "Unknown lastname"
        Account._number_created += 1

    # override the __str__ method
    def __str__(self):
        return f'Bank account has a balance ${self.__balance}'

    def __bool__(self):
        # if self.__balance > 0:
        #     return True
        # else:
        #     return False
        return True if self.__balance > 0 else False

    def __repr__(self):
        return self.__str__()

    # reading
    def get_firstname(self):
        return self._firstname.capitalize()

    # writing
    def set_firstname(self, new_firstname):
        self._firstname = new_firstname

    @property
    def lastname(self):
        return self._lastname

    @lastname.setter
    def lastname(self, new_lastname):
        self._lastname = new_lastname


    # getter to read a piece of data
    def get_balance(self):
        return self.__balance
    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    # getter to read a piece of data
    def get_balance(self):
        return self.__balance


# encapsulation
# loose coupling
# high cohesion - putting things together that belong together.
# abstraction
# inheritance
# polymorphism
