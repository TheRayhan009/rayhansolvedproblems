import math
candel,hulp_candel=map(int,input().split())
time = candel
sm_cndel=candel
len=candel*candel
for i in range(len):
    if sm_cndel>1:
        sm_cndel=int(sm_cndel/hulp_candel)
        time=time+sm_cndel
    else:
        break
print(time)
#problem level : 1000