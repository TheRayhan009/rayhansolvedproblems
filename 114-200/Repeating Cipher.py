st_len=int(input())
st=input()
x=0
ans=[]
# for i in range(0,st_len,x):
#     ans.append(st[i])
#     x+=2
i=1
while st_len>x:
    ans.append(st[x])
    x+=i
    i+=1
print(*ans,sep="")