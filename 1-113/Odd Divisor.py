#problem : TIME_LIMIT_EXCEEDED
oparation=int(input())
for i in range(oparation):
    number=int(input())
    m=1
    for j in range(3,number+3,2):
        if number % j == 0:
            print("YES")
            m=0
            break
    
    if m==1:
        print("NO")