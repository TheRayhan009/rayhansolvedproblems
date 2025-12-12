a,b=map(int,input().split())
year=0
if a==b:
    year=1
    print(year)
else:
    while True:
        if a<=b:
            year=year+1
            a=a*3
            b=b*2
        elif a>b :
            break
    print(year)