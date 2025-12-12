n=int(input())
for i in range(n):
    ans=0
    x=int(input())
    st=input()
    for j in range(x):
        if st[j]=="0":
            ans+=st.count("1")+1
        else:
            ans+=st.count("1")-1
    print(ans)