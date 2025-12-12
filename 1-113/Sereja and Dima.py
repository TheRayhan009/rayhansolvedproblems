numbers_of_cads=int(input())
cads=list(map(int,input().split()))
points_of_Sereja=0
points_of_Dima=0
for i in range(1,numbers_of_cads+1):
    if cads[0]>cads[-1] and i % 2 != 0:
        points_of_Sereja = points_of_Sereja + cads[0]
        cads.remove(cads[0])
    elif cads[0]<cads[-1] and i % 2 != 0:
        points_of_Sereja = points_of_Sereja + cads[-1]
        cads.remove(cads[-1])
    elif cads[0]>cads[-1] and i % 2 == 0:
        points_of_Dima = points_of_Dima + cads[0]
        cads.remove(cads[0])
    elif cads[0]<cads[-1] and i % 2 == 0:
        points_of_Dima = points_of_Dima + cads[-1]
        cads.remove(cads[-1])
    elif len(cads)==1 and i % 2 != 0:
        points_of_Sereja = points_of_Sereja + cads[0]
    elif len(cads)==1 and i % 2 == 0:
        points_of_Dima = points_of_Dima + cads[0]
print(points_of_Sereja,points_of_Dima)