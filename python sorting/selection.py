a=[5,9,1,25,2,65,34,21]
for i in range(len(a)):
    smallest=min(a[i:])
    sindex=a.index(smallest)
    a[i],a[sindex]=a[sindex],a[i]
print(a)
