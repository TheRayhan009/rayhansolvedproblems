st=input()
list_st=list(map(str,input().split()))
x=0
for i in range(len(list_st)):
    if st[0] in list_st[i]:
        x=1
        print("YES")
        break
    if st[1] in list_st[i]:
        x=1
        print("YES")
        break
if x==0:
    print("NO")