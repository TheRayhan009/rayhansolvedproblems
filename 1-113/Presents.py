l=int(input())
a = list(map(int, 
    input().strip().split()))[:l]
ans=""
j=" "
m=0
for i in range(1,l+1):
    z=i
    x=a.index(i)
    m =+ x+1
    m=str(m)
    ans=ans+m+j
    m=str(m)
#ans=str(ans)
print(ans)