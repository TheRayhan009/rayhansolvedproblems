#problem :  TIME_LIMIT_EXCEEDED.
lines=int(input())
for i in range(lines):
    ans=0
    d=0
    a,b=map(int,input().split())
    # if a==b:
    #     print(0)
    if a<b:
        for j in range(min(a,b)):
            if a+10<b:
                ans = ans + 1
                a = a + 10
            elif d==1:
                break
            for x in range(1,11):
                if a+x==b:
                    ans = ans + 1
                    d=1
                    break
    else:
        for j in range(min(a,b)):
            if a>b+10:
                ans = ans + 1
                a = a - 10
            elif d==1:
                break
            for x in range(1,11):
                if a-x==b:
                    ans = ans + 1
                    d=1
                    break
    print(ans)

            
