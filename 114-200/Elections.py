oparetions=int(input())
for i in range(oparetions):
    a,b,c=map(int,input().split())
    max_vot=max(a,b,c)
    if a==0 and b==0 and c==0:
        print("1 1 1")
    else:
        res1 = max(max_vot - a + 1, 0)
        res2 = max(max_vot - b + 1, 0)
        res3 = max(max_vot - c + 1, 0)
        print(res1,res2,res3)