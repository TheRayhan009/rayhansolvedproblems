oparations=int(input())
for i in range(oparations):
    looks=int(input())
    ans=[]
    first_loc=list(map(int,input().split()))
    for j in range(len(first_loc)):
        opar_num=first_loc[j]
        up_down_moves=input()
        for k in range(2,len(up_down_moves)):
            if up_down_moves[k]=="U":
                opar_num=opar_num-1
                if opar_num<0:
                    opar_num=9
            elif up_down_moves[k]=="D":
                opar_num=opar_num+1
                if opar_num==10:
                    opar_num=0
        ans.append(opar_num)
    print(*ans,sep=" ")