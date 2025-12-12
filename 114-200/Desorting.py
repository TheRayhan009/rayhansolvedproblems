#problem : Test: #2, time: 1000 ms., memory: 1272 KB, exit code: -1, checker exit code: 0, verdict: TIME_LIMIT_EXCEEDED
oparetion=int(input())
for i in range(oparetion):
    list_len=int(input())
    num_list=list(map(int,input().split()))
    copy_list=num_list.copy()
    copy_list.sort()
    opa=0
    if copy_list!=num_list:
        print("0")
    else:
        x=num_list[list_len-1]
        y=num_list[list_len-2]
        
        for j in range(x+y):
            if x>=y:
                x-=1
                y+=1
                opa+=1
            else:
                print(opa)
                break