import math
l=int(input())
if l%2==0:
    ans=l/2
    ans=int(ans)
else:
    ans=l/2
    ans=math.ceil(ans)
    ans=ans * -1
print(ans)
# ans=0
# for i in range(1,l+1):
#     if i%2!=0:
#         i = i * -1
#     ans=ans+i
# print(ans)