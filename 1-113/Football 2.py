oparations=int(input())
goles=[]
ans=0
ans2=""
for i in range(oparations):
    input1=input()
    goles.append(input1)
sets=set(goles)
sets=list(sets)
for j in range(len(sets)):
    x=0
    x=goles.count(sets[j])
    if x>ans:
        ans=x
        ans2=sets[j]
print(ans2)