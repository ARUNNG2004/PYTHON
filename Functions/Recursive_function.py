#Recursive_function
def factorial(x):
    if x==0:
        return 1
    else:
        return (x*factorial(x-1))
print("Factorial",factorial(0))