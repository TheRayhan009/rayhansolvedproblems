oparetion=int(input())
for i in range(oparetion):
    num_list_len=int(input())
    num_list=list(map(int,input().split()))
    sum=0
    abvarage=0
    extra_L=0
    exit_No=False
    extra_L_chak=True
    for j in range(num_list_len):
        sum=sum+num_list[j]
    abvarage=sum//num_list_len #2
    for x in range(num_list_len):
        if num_list[x]>=abvarage:
            extra_L=extra_L + abs(abvarage-num_list[x]) 
        elif num_list[x]<abvarage:
            l=abvarage-num_list[x] #l=1
            if extra_L>=l:
                extra_L-=l
            else:
                exit_No=True
                extra_L_chak=False
                break
        
    if exit_No==True:
        print("NO")
    elif extra_L==0 and extra_L_chak==True:
        print("YES")
    else:
        print("NO")
            