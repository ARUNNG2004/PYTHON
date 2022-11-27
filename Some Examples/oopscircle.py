class circle():
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return circle.pi*(self.radius**2)
    def circumference(self):
        return 2*circle.pi*self.radius
r=int(input("Enter the number"))
c=circle(r)
print("The area =",c.area())
print("The cirumference=",c.circumference())




















# class student:
#     m1,m2,m3,m4,m5,m6=19,25,41,36,87,55
#     def process(self):
#         sum=student.m1+student.m2+student.m3+student.m4+student.m5+student.m6
#         avg=sum/6
#         print("Total mark =",sum)
#         print("Average marks=",avg)
#         print(student.m1)
#         return
        
# s=student()
# s.process()
# class Employee():
#     def __init__(self,aname,asalary,adegree):
#         self.name=aname  
#         self.salary=asalary
#         self.degree=adegree  
#     workinghours=12
#     def printdetails(self):
#         return f"Name is {self.name},Salary is {self.salary},Degree is {self.degree}"

# arun=Employee("ARUN","200000","B.TECH")
# ranga=Employee("Ranga","200000","B.TECH")
# print(arun)
