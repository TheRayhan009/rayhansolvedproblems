sets=input()
ans=[]
for i in range(1,len(sets)+1,3):
    ans.append(sets[i])
z="abcdefghijklmnopqrestuvwxyz"
ans=set(ans)
x=len(ans)
a=0
for i in range(len(z)):
    if z[i] in ans:
        a=1
        break
if a==1:
    print(x)
else:
    print("0")