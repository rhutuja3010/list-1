place = ["delhi","gujarat","rajastan","punjab","kerala"]
# print(place[::-1])

# marks = ["10", "32", "42", "65", "67", "89", "76", "38", "67"]
# total_marks = 0
# counter = 0
# while counter < len(marks):
#     total_marks = total_marks+int(marks[counter])
#     counter = counter + 1

# i=len(place)-1
# while i>=0:
#     print(place[i])
#     i-=1


i=1
a=[]
while i<=len(place):
    a.append (place[-i])
    i+=1
print(a)