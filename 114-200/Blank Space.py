oparetions=int(input())
for i in range(oparetions):
    num=int(input())
    num_list=list(map(int,input().split()))
    ans=0
    chak=0
    a=0
    n=0
    count=num_list.count(0)
    if count==len(num_list):
        print(count)
    else:
        for j in range(len(num_list)):
            if num_list[j]==0:
                ans+=1
                if chak<ans:
                    chak=ans
            else:
                if a==0:
                    chak=ans
                elif chak<ans:
                    chak=ans
                ans=0
            a=1
        print(chak)

        '''
        dfghjkdjhygh
        '''