k,y=map(int,input().split())
l=list(map(int,input().split()))

# while True:
#     x=True
#     for q in range(k-1):
#         if l[q]>l[q+1]:
#             l[q],l[q+1] = l[q+1] ,l[q]
#             x=False
#     if x:
#         break
l.sort()
ans=0
for i in range(y):
    if l[i]<1:
        ans+= l[i]
print(abs(ans))
