class Person:
    _number_of_ppl = 0
    @classmethod
    def get_person_count(cls):
        return Person._number_of_ppl

    def __init__(self, name, gender, age):
        self._name = name
        self._gender = gender.upper()
        self._age = age
        Person._number_of_ppl +=1

    def __str__(self):
        return "Name: " + self._name + " Gender: " + self._gender + " Age: " + str(self._age)

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name
