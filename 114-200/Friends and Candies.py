oparetion=int(input())
for i in range(oparetion):
    friends=int(input())
    candi_list=list(map(int,input().split()))
    if friends==1:
        print("0")
    else:
        sum=0
        opare=0
        for j in range(friends):
            sum=sum+candi_list[j]
            if candi_list[j]>friends:
                opare+=1
                
        if sum%friends==0:
            print(opare)
        else:
            print("-1")