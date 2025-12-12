oparetion=int(input())
for i in range(oparetion):
    num_list_len=int(input())
    num_list=list(map(int,input().split()))
    if len(set(num_list))==1:
        print("-1")
    else:
        maxx=max(num_list)
        ans=0
        for j in range(num_list_len):
            if num_list[j]==maxx:
                if j==0 or j== num_list_len-1:
                    if j==0:
                        if num_list[j+1]<maxx:
                            ans=j+1
                            break
                    else:
                        if num_list[j-1]<maxx:
                            ans=j+1
                            break
                else:
                    if num_list[j+1]<maxx or num_list[j-1]<maxx:
                        ans=j+1
                        break
        print(ans)
    