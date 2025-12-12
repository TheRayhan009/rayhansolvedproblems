st_len=int(input())
st=input()
f=""
l=""
if st_len%2==0:
    for i in range(st_len):
        if i%2!=0:
            l=l+st[i]
        else:
            f=st[i]+f
else:
    for i in range(st_len):
        if i%2==0:
            l=l+st[i]
        else:
            f=st[i]+f
print(f+l)
    