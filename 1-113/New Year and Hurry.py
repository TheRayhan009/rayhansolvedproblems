price_of_shovels,onther_coine=map(int,input().split())
i=1
while True:
    x=price_of_shovels*i
    if x%10==onther_coine or x%10==0:
        print(i)
        break
    i = i + 1