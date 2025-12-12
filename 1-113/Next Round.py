a,b=map(int,input().split())
l=input().split()
x=b-1
n=l[x]
count=0
for i in range(a):
    if int(l[i])>=int(n) and l[i]!="0":
        count=count+1
print(count)