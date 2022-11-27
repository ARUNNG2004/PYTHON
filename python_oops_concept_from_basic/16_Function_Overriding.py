class Employee:
    def WorkingHrs(self):
        self.hrs=50
    def printHrs(self):
        print("Total Working Hours : ",self.hrs)

class Trainee(Employee):
    def WorkingHrs(self):
        self.hrs=60
    def resethours(self):
        super().WorkingHrs()

employee=Employee()
employee.WorkingHrs()
employee.printHrs()    

trainee=Trainee()
trainee.WorkingHrs()
trainee.printHrs()
trainee.resethours()
trainee.printHrs()