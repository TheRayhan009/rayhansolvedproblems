have_2,have_3,have_5,have_6=map(int,input().split())
final_ans=0
while True:
    if have_2>0 and have_5>0 and have_6>0:
        final_ans+=256
        have_2-=1
        have_5-=1
        have_6-=1
    elif have_3>0 and have_2>0:
        final_ans+=32
        have_3-=1
        have_2-=1
    else:
        break
print(final_ans)