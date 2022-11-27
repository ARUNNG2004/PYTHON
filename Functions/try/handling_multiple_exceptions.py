#handling multiple exception

try:
    a=10/20
  
    print(a)
    b=[10,20,30,40]
    print(b[10])
except ZeroDivisionError:
    print("denominator can be zero")

except IndexError:
    print("Out of range")


