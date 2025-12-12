a=input()
b=input()
big=0
small=0
a=a.lower()
b=b.lower()
x=0
for i in range(0,len(a)):
    if a==b:
        x=1
 
    else :
        if a>b:
            big=big=1
        elif a<b:
            small=small+1

if x==1:
    print("0")
elif small>big:
    print("-1")
else :
    print("1")