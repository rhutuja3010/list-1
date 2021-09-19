num=[50,40,23,70,56,12,5,10,7]
length=len(num)
i=0
less_than40=0
more_than20=0
while i<length:
    number=num[i]
    if number<40:
        less_than40+=1
    else:
        more_than20+=1
    i+=1
print("less_than40=",(str(less_than40)))
print("more_than20=",(str(more_than20)))
