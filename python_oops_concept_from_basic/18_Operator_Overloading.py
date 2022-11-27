class Additoin:
    def __init__(self,a):
        self.a=a

    def __add__ (o1,o2):
        return o1.a+o2.a
    def __sub__ (o1,o2):
        return o1.a-o2.a
o1=Additoin(10)
o2=Additoin(20)
print("Adding of a",(o1+o2))
print("Difference of a",(o1-o2))