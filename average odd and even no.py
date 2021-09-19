element=[23,14,56,12,19,9,15,25,31,42,43]
i=0
a=0
b=0
while i<len(element):
    if element[i]%2==0:
        print(element[i],"even")
        a+=element[i]
    else:
        print(element[i],"odd")
        b+=element[i]
    i+=1
aveg=a/4
print("average of even no",aveg)
aveg=b/7
print("average of odd no.",aveg)