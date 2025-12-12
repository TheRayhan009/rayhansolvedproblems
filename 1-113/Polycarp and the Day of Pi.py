oparations=int(input())
for i in range(oparations):
    looks=input()
    x="314159265358979323846264338327950288419716939937"
    ans=0
    for j in range(len(looks)):
        if looks[j]==x[j]:
            ans=ans+1
        else:
            break
        
    print(ans)