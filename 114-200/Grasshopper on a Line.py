oparetion=int(input())
for i in range(oparetion):
    num,dividoer=map(int,input().split())
    x=num
    y=0
    move_list=[]
    if num%dividoer!=0:
        move_list.append(num)
        print(len(move_list))
        print(*move_list,sep=" ")
    else:
        for j in range(num):
            x-=1
            y+=1
            if x % dividoer != 0 and y % dividoer != 0:
                move_list.append(x)
                move_list.append(y)
                print(len(move_list))
                print(*move_list,sep=" ")
                break