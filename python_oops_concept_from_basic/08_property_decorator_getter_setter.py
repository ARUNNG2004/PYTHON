
class student:

    def __init__(self,total) -> None:
        self._total=total
    def average(self):
        return self._total/6.0
    @property
    def total(self):
        return self._total
    #
    @total.setter
    def total(self,t):
        if t<0 or t>500:
            print("Invalid Total and can't change")

        else:
            self._totla=t     

o=student(437)
print("Total : ",o.total)
print("Average : ",o.average())
o.total=530
print("Total : ",o.total)
print("Average : ",o.average())
#getter 
