oparetions=int(input())
for i in range(oparetions):
    num_len=int(input())
    st=input()
    right_and_left=0
    up_and_down=0
    a=0
    for j in range(num_len):
        if right_and_left==1 and up_and_down==1:
            a=1
            print("YES")
            break
        elif st[j]=="R":
            right_and_left=right_and_left+1
        elif st[j]=="L":
            right_and_left=right_and_left-1
        elif st[j]=="U":
            up_and_down=up_and_down+1
        elif st[j]=="D":
            up_and_down=up_and_down-1
    if right_and_left==1 and up_and_down==1 and a==0:
            print("YES")
    elif a==0:
        print("NO")