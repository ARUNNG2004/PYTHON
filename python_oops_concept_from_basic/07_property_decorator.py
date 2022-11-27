
class user :
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
        #self.msg=self.name +" is "+str(self.age)+" year old"
    @property
    def msg(self):
        return self.name +" is "+str(self.age)+" year old"

   
a=user("Surya",35)
print(a.msg)
#a.printall()
a.age=34
print(a.msg)