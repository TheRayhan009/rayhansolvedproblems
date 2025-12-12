days=int(input())
prog_of_days=list(map(int,input().split()))
maximum_prog=0
prog=1
for i in range(0,days-1):
    if prog_of_days[i] <= prog_of_days[i+1]:
        prog+=1
        if prog>maximum_prog:
            maximum_prog=prog
    else:
        prog=1
if maximum_prog==0:
    print(prog)
else:
    print(maximum_prog)