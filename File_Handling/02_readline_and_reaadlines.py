try:
    file=open("D://Projects_Working_Space//Python//newwwork2022//File_Handling//first.txt","r")
    #print(file.readline())
    #print(file.readline())
    print(file.readlines())
except FileNotFoundError:
    print("Error File not found")

else:
    file.close()