oparetions=int(input())
for i in range(oparetions):
    num_len=int(input())
    list_1=list(map(int,input().split()))
    list_2=list(map(int,input().split()))
    list_1_min=min(list_1)
    list_2_min=min(list_2)
    ans=0
    for j in range(num_len):
        sbutractino_list_1=list_1_min-list_1[j]
        sbutractino_list_2=list_2_min-list_2[j]
        if sbutractino_list_1==0 and sbutractino_list_2 != list_2_min:
            ans+=sbutractino_list_2
        elif sbutractino_list_1 != list_1_min and sbutractino_list_2==0:
            ans+=sbutractino_list_1
        else:
            x=0
            while x<3:
                if sbutractino_list_1 != list_1_min and sbutractino_list_2 != list_2_min:
                    sbutractino_list_1 -= 1
                    sbutractino_list_2 -= 1
                    ans += 1
                elif sbutractino_list_1 != list_1_min and sbutractino_list_2 == list_2_min:
                    sbutractino_list_1 -= 1
                    ans += 1
                elif sbutractino_list_1 == list_1_min and sbutractino_list_2 != list_2_min:
                    sbutractino_list_2 -= 1
                    ans += 1
                else:
                    break
                x+=1
    print(abs(ans))
