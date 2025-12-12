oparations=int(input())
ans=0
y=""
for i in range(oparations):
    magnets=input()
    if y!=magnets:
        ans+=1
        y=magnets
print(ans)
