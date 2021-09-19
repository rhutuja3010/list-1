elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
count=0
count1=0
while i<len(elements):
    if elements[i]%2==0:
        print(elements[i],"even")
        count+=1
    else:
        print(elements[i],"odd")
        count1+=1
    i+=1
print("sum of even no.=",count)
print("sum of odd no.=",count1)
