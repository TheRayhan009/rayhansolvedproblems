n=int(input())
for i in range(n):
    a=int(input())
    l=list(map(int,input().split()))
    max_num=max(l)
    min_num=min(l)
    found_big_one=True
    found_small_one=True
    two_point_move = 0
    for j in range(0,len(l)):
        if found_big_one:
            two_point_move+=1
            
        if found_small_one:
            two_point_move+=1
            
        if l[j]==max_num or l[a-(j+1)]== max_num:
            found_big_one=False
        if l[j]==min_num or l[a-(j+1)]== min_num:
            found_small_one=False

            
    q=l.index(max_num)
    w=l.index(min_num)
    move_from_left_max= max(q,w)+1
    move_from_left_min= a - min(q,w)
    # print(move_from_left_max)
    # print(move_from_left_min)
    # print(two_point_move)
    
    print(min(two_point_move,move_from_left_max,move_from_left_min))
    
    
            