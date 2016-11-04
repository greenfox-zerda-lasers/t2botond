# Create a student Class
# that has a method `add_grade`, that takes a grade from 1 to 5
# an other method `get_average`, that returns the average of the
# grades
class Student():
    grades=[]

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average(self):
        m = 0
        for i in range(len(self.grades)):
            m = m + self.grades[i]
        return m / len(self.grades)

eva = Student()
eva.add_grade(5)
eva.add_grade(4)
eva.add_grade(3)
eva.add_grade(2)
eva.add_grade(1)
print(eva.get_average())
