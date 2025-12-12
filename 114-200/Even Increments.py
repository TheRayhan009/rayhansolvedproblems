oparetions=int(input())
for i in range(oparetions):
    num_list_len=int(input())
    num_list=list(map(int,input().split()))
    chak1=False #oddindex
    chak2=False #evenindex
    if num_list[0]%2==0:
        for oddindex in range(0,num_list_len,2):
            if num_list[oddindex]%2==0:
                chak1=True
            else:
                chak1=False
                break
    if num_list[0]%2!=0:
        for oddindex in range(0,num_list_len,2):
            if num_list[oddindex]%2!=0:
                chak1=True
            else:
                chak1=False
                break
    if num_list[1]%2==0:
        for evenindex in range(1,num_list_len,2):
            if num_list[evenindex]%2==0:
                chak2=True
            else:
                chak2=False
                break
    if num_list[1]%2!=0:
        for evenindex in range(1,num_list_len,2):
            if num_list[evenindex]%2!=0:
                chak2=True
            else:
                chak2=False
                break
    if chak1==True and chak2==True:
        print("YES")
    else:
        print("NO")