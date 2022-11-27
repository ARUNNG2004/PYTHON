


par=[]
print("enter para")
while True:
    line=input()
    if line:
        par.append(line)
    else:
        break
print(par)
ooutput='\n'.join(par)
print(ooutput)