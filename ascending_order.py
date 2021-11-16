list=[5,0,1,8,2,6,3,9,4,7]
for j in range(len(list)):
    for i in range(len(list)-1):
        if list[i]>list[i+1]:
            a=list[i]
            list[i]=list[i+1]
            list[i+1]=a
print(list)

l=[5,0,1,8,2,6,3,9,4,7]
i=0
while i<len(l):
    j=0
    while j<len(l)-1:
        if l[j]>l[j+1]:
            a=l[j]
            l[j]=l[j+1]
            l[j+1]=a
        j+=1
    i+=1
print(l)

list=[5,0,1,8,2,6,3,9,4,7]
i=0
while i<len(list):
    j=0
    while j<len(list)-1:
        if list[j]>list[j+1]:
            a=list[j]
            list[j]=list[j+1]
            list[j+1]=a
        j+=1
    i+=1
print(list)