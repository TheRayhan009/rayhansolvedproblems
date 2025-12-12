oparetions=int(input())
for i in range(oparetions):
    stiks=int(input())
    ans=1
    if stiks%2==0:
        sub_stiks=stiks-2
        ans=ans+int(sub_stiks/2)
    else:
        sub_stiks=stiks-1
        ans=ans+int(sub_stiks/2)
    print(ans)