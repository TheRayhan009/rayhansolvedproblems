num_len=int(input())
num_list=list(map(int,input().split()))
ans=0
a=0
chak=0
for j in range(len(num_list)-1):
    if num_list[j]<num_list[j+1]:
        ans+=1
    else:
        if ans>chak:
            chak=ans+1
        ans=0
print(chak+1)