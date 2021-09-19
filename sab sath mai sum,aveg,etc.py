element=[23,14,56,12,19,9,15,25,31,42,43]
i=0
a=0
b=0
count=0
count1=0
while i<len(element):
    if element[i]%2==0:
        print(element[i],"even")
        a=a+element[i]
        count+=1
    else:
        print(element[i],"odd")
        b=b+element[i]
        count1+=1
    i+=1
print("sum of even no.",a)
average=a/4
print("average=",average)
print("sum of odd no.",b)
average=b/7
print("average=",average)
print(count,"total even no.")
print(count1,"total odd no.")