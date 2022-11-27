class sample:
    num=0
    def __init__(self,var):
        sample.num+=1
        self.var=var
        print("The oject",var)
        print(sample.num)
        def __del__(self):
            sample.num-=1
            print ("gfhd")
s1=sample(15)
s2=sample(16)
s3=sample(13)