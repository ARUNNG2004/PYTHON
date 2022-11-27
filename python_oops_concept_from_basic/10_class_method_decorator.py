class student:
    count=0
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
        student.count+=1

    def printdetails(self):
        print("Name",self.name ," age ",self.age)
    
    @classmethod
    def totalcount(co):
        return co.count
b=student("Shreya",18)
b.printdetails()

print("Total Admission :",student.totalcount())
c=student("Raja",23)
c.printdetails()

print("Total Admission :",student.totalcount())
c=student("samy",48)
c.printdetails()
print("Total Admission :",student.totalcount())