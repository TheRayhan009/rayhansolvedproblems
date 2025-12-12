q,w=map(int,input().split())
l = list(input())
chak=False
for i in range(w):
    x=0
    while x<q-1:
        if l[x]=="B" and l[x+1]=="G":
            l[x],l[x+1] = l[x+1],l[x]
            x+=2
        else:
            x+=1     
print("".join(l))