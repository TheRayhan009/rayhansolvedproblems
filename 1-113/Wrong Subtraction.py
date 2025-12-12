a,b=map(int,input().split())
for i in range(b):
    if str(a)[-1]=='0':
        a=int(a/10)
        b=b+1
    else:
        a=a-1
print(a)
# 512
# 511
# 510
# 
# 
