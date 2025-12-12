# problem : Test: #4, time: 2000 ms., memory: 63660 KB, exit code: -1, checker exit code: 0, verdict: TIME_LIMIT_EXCEEDED
oparetion=int(input())
for i in range(oparetion):
    f_list_len,s_list_len=map(int,input().split())
    f_list=input()
    s_list=input()
    chak=False
    count=0
    if s_list in f_list:
        print(count)
    else:
        for j in range(s_list_len):
            if s_list in f_list:
                chak=False
                break
            else:
                f_list+=f_list
                count+=1
                chak=True
            if count>s_list_len:
                chak=True
                break
                
        if chak==True:
            print("-1")
        else:
            print(count)