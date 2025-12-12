oparations=int(input())
for i in range(oparations):
    ans=0
    ans2=[]
    lines=int(input())
    nums=list(map(int,input().split()))
    for j in range(len(nums)):
        if nums[j]>ans and str(nums[j]) not in ans2 or nums[j]<ans and str(nums[j]) not in ans2:
            ans=nums[j]
            ans2.append(str(nums[j]))
    print(*ans2,sep=" ")