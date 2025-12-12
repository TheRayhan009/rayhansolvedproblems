# oparetion,cpuL,memoryL=map(int,input().split())
# jug_ans=[]
# for i in range(0,oparetion):
#     output,cpu,memory=map(int,input().split())
#     if cpu>cpuL:
#         jug_ans.append("CLE")
#     elif memory>memoryL:
#         jug_ans.append("MLE")
#     elif output!=0:
#         jug_ans.append("WA")
#     else:
#         jug_ans.append("AC")

# # print(jug_ans)
# if "CLE" in jug_ans:
#     print("CLE")
# elif "MLE" in jug_ans:
#     print("MLE")
# elif "WA" in jug_ans:
#     print("WA")
# else:
#     print("AC")

import math
n=int(input())
for i in range(n):
    num=int(input())
    sq=False
    for j in range(1,math.sqrt(num)+1):
        if j*j==num:
            sq=True
    if sq==True:
        print("YES")
    else:
        print("NO")