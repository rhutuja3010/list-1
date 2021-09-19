q= [
    "How many continents are there?",              
    "What is the capital of India?",            
    "NG mei kaun se course padhaya jaata hai?"    
]

Opt= [
    ["Four", "Nine", "Seven", "Eight"],
    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"]]
s=[3,4,1]
ans=[["(3)Seven","(4)Eight"],
["(3)Chennai","(4)Delhi"],
["(1)Software Engineering","(2)Counseling"]]
print("koun banega corodepati(KBC)")
i=0
x=0
count=0
while i<len(q):
    print(q[i])
    a=0
    b=i
    while x<=len(Opt[i]):
        y=Opt[i][a]
        print(a+1,y)
        a+=1
    lifeline=input("do you have 50-50lifeline:")
    if lifeline=="yes":
        print("accept")
        if count<1:
            print(ans[b])
            num=int(input("enter your ansewer:"))
            if num==(x[i]):
                print("correct answer")
                x+=100
                print("win",x)
            else:
                print("incorrect answer")
                print("win",x)
                break
            count+=1
        else:
            print("you already use lifeline")
            num1=int(input("enter your answer="))
            if num1==s[i]:
                print("congrats, your answer is correct")
                s+=100
                print("win",x)
            else:
                print("your answer is wrong")
                print("win",x)
                break
    else:
        num3=int(input("enter your answer="))
        if num3==s[i]:
            print("correct your answer")
            x+=100
            print("win",x)
        else:
            print("no chance")
            print("your answer is wrong")
            print("win",x)
    i+=+1
print("win",x)
print("thanks and congragulation")
            
    
    
     
    
