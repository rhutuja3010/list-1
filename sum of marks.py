# marks=[[78,76,94,86,88],
#       [91,71,98,65,76],
#       [95,45,78,52,49]]
# i=0
# count=0
# while i<len(marks):
#     j=0
#     sum=0
#     a=0
#     while j<len(marks[i]):
#         a=a+(marks[i][j])
#         j+=1
#     sum+=a
#     average=sum//len(marks[i])
#     i+=1
#     count+=1
#     print(count,"year average=",average)
marks=[[78,76,94,86,88],
      [91,71,98,65,76],
      [95,45,78,52,49]]
i=0
sum=0
while i<len(marks):
    j=0
    sum1=0
    while j<len(marks[i]):
        sum+=(marks[i][j])
        j+=1
    i+=1
print(sum)
    
        
        