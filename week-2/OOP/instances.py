# import class Employee from moddule employee
from employee import Employee
# import class Person from module person
from person import Person

# instantiate Person with arguments for name, gender and age and assign it to a variable weronika
weronika = Person("Weronika", 'f', 32)
# print Person weronika
print(weronika)

# instantiate kamil Employee object
kamil = Employee("Kamil", 'm', 33, 'IT', '1250L')
print(kamil)

nathan = Employee("Nathan", 'm', 27, 'IT', '999')
print(nathan)

# nathan change tax code for nathan object
nathan.set_tax('10000K')
print(nathan.get_tax())

# print number of people created
print(Person.get_person_count())
