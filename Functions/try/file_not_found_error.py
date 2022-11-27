#file_not_found_error

try:
    f=open("test.txt")
except FileNotFoundError:
    print("File not found")

else:
    print(f.read())
