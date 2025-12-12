year =int (input())
while True:
    year=year+1
    y=str(year)
    if y[0]!=y[1] and y[1] != y[2] and y[1] != y[3] and y[2] != y[0] and y[3] != y[0] and y[2] != y[3] :
        print (y)
        break
    