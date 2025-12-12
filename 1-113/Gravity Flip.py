# l=int(input())
# a = input()
# a=list(a)
# ans=sorted(a)
# # ans=' '.join(a)
# print(*ans)
    

l = int(input())
a = list(map(int, input().split()))
ans = sorted(a)
print(*ans)