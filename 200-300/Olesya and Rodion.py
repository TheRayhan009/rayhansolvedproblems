n,m=map(int,input().split())
if m==2:
    print("2"+ "0"*(n-1) )
elif m==3:
    print("3"+ "0"*(n-1) )
elif m==4:
    print("4"+ "0"*(n-1) )
elif m==5:
    print("5"+ "0"*(n-1) )
elif m==6:
    print("6"+ "0"*(n-1) )
elif m==7:
    print("7"+ "0"*(n-1))
elif m==8:
    print("8"+ "0"*(n-1) )
elif m==9:
    print("9"+ "0"*(n-1))
elif m==10 and n!=1:
    print("10"+ "0"*(n-2))
else:
    print(-1)