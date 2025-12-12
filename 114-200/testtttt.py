import sys
sys.set_int_max_str_digits(430000000)
oparetion=int(input())
for i in range(1,oparetion+1):
    num1,num2=map(str,input().split())
    print(f"Case #{str(i)}:",int(num1)+int(num2))