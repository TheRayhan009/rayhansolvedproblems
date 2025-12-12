# have some problem
oparetion=int(input())
for i in range(oparetion):
    list_lenth,nums=map(int,input().split())
    a_list=list(map(int,input().split()))
    for x in range(nums):
        l,r,k=map(int,input().split())
        ans=0
        x=a_list
        print(x)
        for j in range(l,r+1):
            if x[j-1]!=k:
                x[j-1]=k
        for o in x:
            ans+=o
        print(x)
        print(ans)
        if ans%2==0:
            print("NO") 
        else:
            print("YES")
        x=[]
        
            