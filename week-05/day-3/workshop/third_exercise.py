# Write a Person class that have a name and a birth_date property
# It should raise an error of the birthdate is less than 0 or more than 2016
class Person:
    def __init__(self, _name, _birth_date):
        if _birth_date < 0 or _birth_date > 2016:
            raise ValueError
        self.name = _name
        self.birth_date = _birth_date

#person1 = Person("Bela",11923)
#print(person1.name)
