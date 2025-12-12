oparations=int(input())
for i in range(oparations):
    #codeforces
    st=input()
    chak="codeforces"
    ans=0
    for j in range(len(st)):
        if st[j]!=chak[j]:
            ans=ans+1
    print(ans)
