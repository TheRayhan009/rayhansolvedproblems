oparetion=int(input())
for i in range(oparetion):
    l_1=input()
    l_2=input()
    main_list=[]
    main_list.append(l_1[0])
    main_list.append(l_1[1])
    main_list.append(l_2[0])
    main_list.append(l_2[1])
    set_list=set(main_list)
    set_list=list(set_list)
    chak_list=[]
    for j in range(len(set_list)):
        chak_list.append(main_list.count(set_list[j]))
    print(len(chak_list)-1)