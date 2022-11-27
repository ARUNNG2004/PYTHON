class A:
    def display(self):
        print("I am the display of  class a")

class B(A):
    def display(self):
        print("I am the display of  class B")
               
class C(A):
    def display(self):
        print("I am the display of  class C")


class D(B,C):
    def display(self):
        print("I am the display of  class D")
          

o=D()
o.display()
