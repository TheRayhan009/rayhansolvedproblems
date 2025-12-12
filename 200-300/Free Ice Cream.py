oparetion,total_ice_cream=map(int,input().split())
not_goten_childs=0
for i in range(oparetion):
    st=input().split(" ")
    # print(st)
    
    if st[0]=="+":
        total_ice_cream+=int(st[1])
        
    else:
        if total_ice_cream>=int(st[1]):
            total_ice_cream-=int(st[1])
        else:
            not_goten_childs+=1
print(total_ice_cream,not_goten_childs)