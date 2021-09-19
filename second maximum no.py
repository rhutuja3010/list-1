# number=[50,40,23,70,56,12,5,10,7]
# i=0
# x=number[0]
# while i<len(number):
#     if number[i]>x:
#      x=number[i]
#     i=i+1
# number.remove(x)
# y=number[0]
# i=0
# while i<len(number):
#     if number[i]>y:
#      y=number[i]
#     i=i+1
# print(y)

# 

number=[50,40,23,70,56,12,5,10,7]
i=0
a=70
b=56
a,b=b,a
while i<len(number):
    if number[i]>a:
        b=number[i]
    i=i+1
print(a)

