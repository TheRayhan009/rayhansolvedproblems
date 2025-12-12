#Problem : Test: #4, time: 1000 ms., memory: 9076 KB, exit code: -1, checker exit code: 0, verdict: TIME_LIMIT_EXCEEDED

oparetion=int(input())
for i in range(oparetion):
    list_len=int(input())
    p_a=input().split()
    p_b=input().split()
    p_c=input().split()
    p_a_ans=0
    p_b_ans=0
    p_c_ans=0
    for x in range(list_len):
        q=1
        s=1
        t=1
        y=p_b.count(p_a[x])
        y2=p_c.count(p_a[x])
        t+=y+y2
        if t==1:
            p_a_ans+=3
        if t==2:
            p_a_ans+=1
        y=p_a.count(p_b[x])
        y2=p_c.count(p_b[x])
        q+=y+y2
        if q==1:
            p_b_ans+=3
        if q==2:
            p_b_ans+=1
        y=p_a.count(p_c[x])
        y2=p_b.count(p_c[x])
        s+=y+y2
        if s==1:
            p_c_ans+=3
        if s==2:
            p_c_ans+=1
    print(p_a_ans," ",p_b_ans," ",p_c_ans,)