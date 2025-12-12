list_len=int(input())
num_list=list(map(int,input().split()))
chest=True
biceps=False
back=False
chest_sum=0
biceps_sum=0
back_sum=0
for j in range(list_len):
    if chest==True:
        chest_sum+=num_list[j]
        chest=False
        biceps=True
    elif biceps==True:
        biceps_sum+=num_list[j]
        biceps=False
        back=True
    elif back==True:
        back_sum+=num_list[j]
        back=False
        chest=True
if max(chest_sum,biceps_sum,back_sum)==back_sum:
    print("back")
elif max(chest_sum,biceps_sum,back_sum)==chest_sum:
    print("chest")
elif max(chest_sum,biceps_sum,back_sum)==biceps_sum:
    print("biceps")
