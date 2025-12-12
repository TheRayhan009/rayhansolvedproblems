oparetion=int(input())
for i in range(oparetion):
    lenx=int(input())
    st0=input()
    st0="0"+st0
    st1=""
    countx=0
    boolst0=True
    boolst1=False
    check=st0[0]
    for j in range(0,lenx):
        if int(st0[j])!=int(st0[j+1]):
            countx+=1
    print(countx)