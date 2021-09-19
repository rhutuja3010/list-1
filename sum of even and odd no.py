element=[23,14,56,12,19,9,15,25,31,42,43]
i=0
a=0
b=0
while i<len(element):
    if element[i]%2==0:
        print(element[i],"even")
        a=a+element[i]
    else:
        print(element[i],"odd")
        b=b+element[i]
    i+=1
print("sum of even no.",a)
print("sum of odd no.",b)

