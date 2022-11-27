from abc import ABC,abstractmethod
class Bank(ABC):
    @abstractmethod
    def Loan(self): pass
    @abstractmethod
    def Credit(self): pass
    @abstractmethod
    def Debit(self): pass

class HDFC(Bank):
    def Loan(self):
        print("We can Providen 7.5% Interest Loan")

    def Credit(self):
        print("HDFC Provide Credit")

    def Debit(self):
        print("HDFC Provide Debit")
o=HDFC()
o.Credit()
o.Debit()
o.Loan()