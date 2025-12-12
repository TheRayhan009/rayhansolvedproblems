oparetion=int(input())
for i in range(oparetion):
    books=int(input())
    time_store_list=[]
    one_time_store_list=[]
    ans=0
    for j in range(books):
        time,skill=map(int,input().split())
        skill=str(skill)
        # first_chak=False
        # secunde_chak=False
        if skill == "01":
            time_store_list.append(time)
        elif skill == "10":
            time_store_list.append(time)
        elif skill == "11":
            one_time_store_list.append(time)
    time_store_list.sort()
    one_time_store_list.sort()
    print(time_store_list)
    print(time_store_list)
    if time_store_list[0]+time_store_list[1] < one_time_store_list[0]:
        ans=time_store_list[0]+time_store_list[1]
        print(ans)
    elif time_store_list[0]+time_store_list[1] > one_time_store_list[0]:
        ans=one_time_store_list
        print(ans)
