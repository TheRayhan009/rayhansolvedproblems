num=int(input())
ans=[]
n=0
x=1
if num==2:
    print("""1
2""")
    x=0
elif num==3:
    print("""1
3""")
    x=0
elif num%2==0:
    for i in range(1,num+1):
        n=i
        num=num-2
        ans.append("2")
        if num==0:
            break
elif num%2!=0:
    for i in range(1,num+1):
        num=num-2
        ans.append("2")
        if num==3:
            num=num-3
            ans.append("3")
        if num==0:
            n=i+1
            break
if x!=0:
    print(n)
    print(*ans,sep=" ")