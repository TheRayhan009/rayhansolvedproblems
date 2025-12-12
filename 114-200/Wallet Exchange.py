oparetion=int(input())
for i in range(oparetion):
    alice,bob=map(int,input().split())
    sum=alice+bob
    if sum%2==0:
        print("Bob")
    else:
        print("Alice")