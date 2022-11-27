# class sample:
#     __num=10
#     def da(self):
#         print(self.__num)
# s=sample()
# s.da()
# # print(s.__num)
class fruits:
    def __init__(self,f1,f2):
        self.f1=f1
        self.f2=f2
    def display(self):
        print("Fruit 1 = %s,Fruit 2 = %s" % (self.f1,self.f2))
f=fruits ('Apple','mango')
f.display
f.display()
