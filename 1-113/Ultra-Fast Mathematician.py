a=input()
b=input()
ans=[]
for i in range(len(a)):
    if a[i]==b[i]:
        ans.append("0")
    else:
        ans.append("1")
ans = ''.join(ans)
print(ans)