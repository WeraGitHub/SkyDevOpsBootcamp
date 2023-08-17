from person import Person

class Employee(Person):
    def __init__(self, name, gender, age, dept, tax):
        super().__init__(name, gender, age)
        self._dept = dept
        self._tax = tax

    def __str__(self):
        return "Name: " + self._name + " Age: " + str(self._age) + "Department: " + self._dept

    def get_tax(self):
        return self._tax

    def set_tax(self, new_tax):
        self._tax = new_tax
