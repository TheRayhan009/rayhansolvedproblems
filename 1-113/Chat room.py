st=input()
h=0
e=0
l=0
o=0
for i in range(len(st)):
    if st[i]=="h":
        h=h+1
    elif st[i]=="e" and h>0:
        e=e+1
    elif st[i]=="l" and e>0:
        l=l+1
    elif st[i]=="o" and l>1:
        o=o+1
if h>0 and e>0 and l>1 and o>0:
    print("YES")
else:
    print("NO")


