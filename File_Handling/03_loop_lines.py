try:
    file=open("D://Projects_Working_Space//Python//newwwork2022//File_Handling//first.txt","r")
    for i in file:
        print(i)
except FileNotFoundError:
    print("Error File not found")

else:
    file.close()