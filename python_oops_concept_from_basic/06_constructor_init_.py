#init method
class user:
    def __init__(self,name):

        print("Call when new instance created")
        self.name=name
    def  printall(self):
        print("Name : ",self.name)

o1=user("vikram")        
o1.printall()

o2=user("secret agent")
o2.printall()