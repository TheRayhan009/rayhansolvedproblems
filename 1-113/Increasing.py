oparetions=int(input())
for i in range(oparetions):
    num_len=int(input())
    nums=list(map(int,input().split()))
    nums.sort()
    chak=0
    for i in range(len(nums)-1):
        if nums[i]==nums[i+1]:
            chak=1
    if chak==1:
        print("NO")
    else:
        print("YES")