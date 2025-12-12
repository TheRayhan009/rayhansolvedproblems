oparations=int(input())
st=input()
x=0
ans=0
for i in range(oparations):
    if x>1 and st[i]=="x":
        ans=ans+1
    elif st[i]=="x":
        x=x+1
    else:
        x=0
print(ans)