# a=[1,0,0,1,1,0,1,1]
# i=1
# sum=0
# while i<len(binary_number):
#     a=binary_number[-i-1]
#     sum=sum+a*2**i
#     i=i+1
# print(sum)

# num=int(input("enter the number"))
# a=int(input("enter the number"))

# a=[1,0,0,1,1,0,1,1]
# a=int(input("enter the any number"))
# i=0
# sum=0
# while a!=0:
#     rem=a/10
#     sum=sum+rem*pow(2,i)
#     a=int(a/10)
#     i=i+1
# print(sum)
a=[1,0,0,1,1,0,1,1]
i=1
j=0
sum=0
while i<=len(a):
    d=a[-i]
    sum=sum+(2**j)*d
    j=j+1
    i=i+1
print(sum)



