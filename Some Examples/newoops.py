# class sample():
#     num=0
#     def __init__(self,var):
#         self.var=var
#         self.var+=1
#         print("the var value",self.var)
#         print (sample.num)
#     def __del__ (self):
#         sample.num-=1
#         print("The var %d value is "%self.var )
# sample(15)
# sample(16)
# sample(11)
class sample():
    a=("Arun is good boy in the world")
    def __init__ (self,n1,n2):
        self.n1=n1
        self.n2=n2
    def condition(self):
        print ("The valuue is good ",self.n1)
        print ("The valuue is good ",self.n2)
        print ("The valuue is good ",sample.a)
    n1=int(input("Enter the number for n1"))
    n2=int(input("Enter the number for n2"))



