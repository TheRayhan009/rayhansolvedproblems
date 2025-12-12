sum_string=input()
numbers=[]
for i in range(len(sum_string)):
    if i%2==0:
        numbers.append(sum_string[i])
numbers.sort()
for i in range(len(numbers)):
    if i==0:
        print(*numbers[i],sep="",end="")
    elif i==len(numbers)-1:
        print(*"+",numbers[i],sep="",end="")
    else:
        print(*"+",numbers[i],sep="",end="")