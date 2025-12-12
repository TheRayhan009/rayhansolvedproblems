l=int(input())
a=input()
count=0
for i in range(0,l-1):
    x=a[i+1]
    if a[i]==x:
        count += 1

print(count)
    