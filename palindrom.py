name=['n','i','t','i','n']
a=[]
i=1
while i<=len(name):
    a.append (name[-i])
    i=i+1
print(a)
if a==name:
    print("it is palindrom")
else:
    print("it is not palindrom")
