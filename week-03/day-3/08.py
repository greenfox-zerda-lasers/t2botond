# Create a new class called `Person` that has a first_name and a last_name (takes it in it's constructor)
# It should have a `greet` method that prints it's full name

# Create a `Student` class that is the child class of `Person`
# it should have a method to add grades
# it should have a `salute` method that prints it's full name and the average of it's grades as well

class Person():

    def addname(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def greet(self):
        print(self.firstname,self.lastname)
        
class Student(Person):
    grades=[]

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average(self):
        m = 0
        for i in range(len(self.grades)):
            m = m + self.grades[i]
        return m / len(self.grades)


beci = Person()

beci.addname('Kovacs', 'Bela')
beci.greet()
eva = Student()
eva.addname('Kovacs', 'Eva')
eva.add_grade(5)
eva.add_grade(4)
eva.add_grade(3)
eva.add_grade(2)
eva.add_grade(1)
eva.greet
print(eva.get_average())
