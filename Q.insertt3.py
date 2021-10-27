a=[2,4,5,7,1,8,9,4]
i=0
b=[]
while i<len(a):
    if i%2!=0:
        b.append(3)
    else:
        b.append(a[i])
    i+=1
print(b)