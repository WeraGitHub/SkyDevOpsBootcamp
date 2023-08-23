from custom_exceptions import WrongPayRaisePercentError


class Employee:
    def __init__(self, firstname, lastname, pay):
        self._firstname = firstname
        self._lastname = lastname
        self._pay = pay

    @property
    def fullname(self):
        return "Bob Ross"

    @property
    def email(self):
        return self._firstname + self._lastname + '@email.com'

    def apply_raise(self, percent):
        if percent > 15:
            raise WrongPayRaisePercentError
        else:
            return self._pay * percent / 100
