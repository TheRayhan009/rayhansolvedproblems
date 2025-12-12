oparations=int(input())
for i in range(oparations):
    st=input()
    num_st=int(st)
    if num_st%2020==0 or num_st%2020<=num_st/2020:
        print("YES")
    else:
        print("NO")