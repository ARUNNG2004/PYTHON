def insertion(mylist):
    for i in range(1,len(mylist)):
        currentvalue=mylist[i]
        k=i-1
        while k>=0 and mylist[k]>currentvalue:
            mylist[k+1]=mylist[k]
            k-=1
        mylist[k+1]=currentvalue
mylist=[2,0,11,31,87,53,52] 
print("Before sorted",mylist)
insertion(mylist)
print("After sorted",mylist)   