#class methods
class Student:
    name="god"
    age=100
    def printall():
        print("Name :",Student.name)
        print("age  :",Student.age)
#  Student.printall()
getattr(Student,'printall')()