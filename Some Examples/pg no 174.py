class sample :
    num=0
    def __init__(self,var):
        sample.num+=1
        self.var=var
        print("the object",self.var)
        print("thecount ",sample.num)
    def __del__ (self):
            sample.num-=1
            print("the object value ",self.var)

s1=sample(15)
s2=sample(35)
s3=sample(45)