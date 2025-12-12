oparetion=int(input())
for i in range(oparetion):
    books=int(input())
    time_store_list=[]
    time_store_list2=[]
    one_time_store_list=[]
    ans=0
    first_chak=False
    sec_chak=False
    all_chak=False
    for j in range(books):
        time,skill=map(str,input().split())
        if skill[0]=="0" and skill[1]=="1":
            time_store_list.append(int(time))
            sec_chak=True
        elif skill[0]=="1" and skill[1]=="0" :
            time_store_list2.append(int(time))
            first_chak=True
        elif int(skill)==11:
            one_time_store_list.append(int(time))
            all_chak=True
    if first_chak==False or sec_chak==False:
        if all_chak==True:
            one_time_store_list.sort()
            print(one_time_store_list[0])
        else:
            print("-1")
    # elif all_chak==False:
    #     print("-1")
    else:
        time_store_list.sort()
        time_store_list2.sort()
        one_time_store_list.sort()
        # if len(one_time_store_list)>0 and len(time_store_list)==0 and len(time_store_list2)==0:
        #     print(one_time_store_list[0])
        if len(one_time_store_list)>0 and len(time_store_list)>0 and len(time_store_list2)>0:
            if time_store_list[0]+time_store_list2[0] > one_time_store_list[0]:
                print(one_time_store_list[0])
            elif time_store_list[0]+time_store_list2[0] < one_time_store_list[0]:
                print(time_store_list[0]+time_store_list2[0])
            elif time_store_list[0]+time_store_list2[0] == one_time_store_list[0]:
                print(time_store_list[0]+time_store_list2[0])
        else:
            print(time_store_list[0]+time_store_list2[0])
    
