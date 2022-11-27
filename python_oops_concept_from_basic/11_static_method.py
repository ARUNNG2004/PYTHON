#static method

class student:
    def __init__(self,name,age) :
        self.name=name
        self.age=age
     
    def printdetails(self):
        print("Name : ",self.name," Age : ",self.age)
    @staticmethod
    def welcome():
        print("Welcome to avs college")
s1=student("ARUN",24)
s1.welcome()
s1.printdetails()

s2=student("Gopi",24)
s2.welcome()
s2.printdetails()
