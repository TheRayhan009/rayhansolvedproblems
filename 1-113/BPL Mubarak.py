oparation=int(input())
for i in range(oparation):
    balls_oparations=input()
    ball=0
    over=0
    for j in range(len(balls_oparations)):
        if balls_oparations[j]!='N' and balls_oparations[j]!='W' and balls_oparations[j]!='D':
            ball=ball+1
    if ball%6==0 and int(ball/6)==1:
        print(int(ball/6),"OVER")
    elif ball%6==0 and int(ball/6)>1:
        print(int(ball/6),"OVERS")
    
