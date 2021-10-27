p=["rhutuja","mom","dad","patil"]
a=[]
b=[]
c=[]
d=[]
for i in range(len(p)):
    for j in range(len(p[i])):
        if i==0:
            a.append(p[i][j])
        if i==1:
            b.append(p[i][j])
        if i==2:
            c.append(p[i][j])
        if i==3:
            d.append(p[i][j])
print(a)
print(b)
print(c)
print(d)
w=a[::-1]
x=b[::-1]
y=c[::-1]
z=d[::-1]
count=1
if a==w:
    print(w,count,"it is palindrom")
    count+=1
if b==x:
    print(x,count,"it is palinpdrom")
    count+=1
if c==y:
    print(y,count,"it is palindrom")
    count+=1
if d==z:
    print(z,count,"it is palindrom")
    count+=1