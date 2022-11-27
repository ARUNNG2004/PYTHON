#value_error

try:
    a=int("BOt")
except ValueError as a:
    print(a,"Please enter numbers only")