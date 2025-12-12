oparation=int(input())
for i in range(oparation):
    st_len=int(input())
    st=input()
    ans=""
    for j in range(st_len):
        if st[j]=="D":
            ans=ans+"U"
        elif st[j]=="U":
            ans=ans+"D"
        else:
            ans=ans+st[j]
    print(ans)