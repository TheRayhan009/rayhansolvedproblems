ls = int (input())
for i in range(ls):
    input1=input()
    ans=''
    for j in range(1,len(input1)-1,2):
        if input1[j]==input1[j+1]:
            ans+=input1[j]
            x=input1[j]
        # else:
        #     ans+=input1[j]
    print(input1[0]+ans+input1[-1])