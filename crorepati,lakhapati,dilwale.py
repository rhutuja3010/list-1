x=[3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
i=0
count=0
count1=0
count2=0
while i<len(x):
    y=x[i]
    if y>10000000:
        count+=1
    elif y>100000:
        count1+=1
    elif y<100000:
        count2+=1
    i+=1
print("crorepati",count)
print("lakhapati",count1)
print("dilavale",count2)
    

    