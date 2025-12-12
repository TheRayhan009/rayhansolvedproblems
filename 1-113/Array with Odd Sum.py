oparetions=int(input())
for i in range(oparetions):
    num_len=int(input())
    nums=list(map(int,input().split()))
    ans=0
    odd=0
    even=0
    for j in range(num_len):
        if nums[j]%2!=0:
            odd+=1
        else:
            even+=1
        ans+=nums[j]
    if ans%2!=0:
        print("YES")
    else:
        if even>0 and odd>0:
            print("YES")
        else:
            print("NO")