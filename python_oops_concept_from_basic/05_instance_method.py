class Student:
    name="god"
    age=100
    def printall(self,gender):
        print("Name :",Student.name)
        print("age  :",Student.age)
        print("Gender  :",gender)
o=Student()
# o.printall()
# instarded of this
# Student.printall(o)
o.printall("Male")
Student.printall(o,"female")