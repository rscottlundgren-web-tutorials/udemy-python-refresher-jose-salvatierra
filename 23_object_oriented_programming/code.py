# student = {"name": "Rolf", "grades": (89, 90, 93, 78, 90)}


# def average(sequence):
#     return sum(sequence)/len(sequence)


# print(average(student["grades"]))
# print(student.average())  # This is what we want ideally

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)


student1 = Student("Brian", (100, 100, 90, 90, 93, 78, 90))
student2 = Student("Scott", (100, 100, 100, 100, 93, 78, 90))

print(student1.name)
print(student1.grades)
print(student1.average_grade())
print(student2.name)
print(student2.grades)
print(student2.average_grade())
