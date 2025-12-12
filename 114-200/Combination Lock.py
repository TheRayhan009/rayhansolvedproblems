list_len=int(input())
clock1=input()
clock2=input()
ans=0
for i in range(list_len):
    step_ans=0
    step_ans2=0
    a=int(clock1[i])
    x=int(clock2[i])

    while a != x:
        if a==10:
            a=0
        if a==x:
            break
        else:
            a+=1
            step_ans+=1
    b=int(clock1[i])
    y=int(clock2[i])
    while b != y:
        if b==-1:
            b=9

        if b==y:
            break
        else:
            b=b-1
            step_ans2+=1   
    if step_ans<step_ans2:
        ans+=step_ans
    else:
        ans+=step_ans2
print(ans)
    
        
