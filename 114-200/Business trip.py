num=int(input())
list_st=list(map(int,input().split()))
len=len(list_st)
list_st.sort()
time=0
ans=0
if sum(list_st)<num:
    print("-1")
else:
    for j in range(len):
        if ans>=num:
            break
        else:
            ans=ans+list_st[-1]
            time+=1
            list_st.pop()
    print(time)
    