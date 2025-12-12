oparetion=int(input())
l=list(map(int,input().split()))
l.sort()
need_problems=0
for j in range(0,oparetion,2):
    need_problems+= (l[j+1]-l[j])
print(need_problems)    