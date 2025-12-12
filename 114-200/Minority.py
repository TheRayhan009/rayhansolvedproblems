oparetion=int(input())
for i in range(oparetion):
    num_liat=list(input())
    one_count=num_liat.count("1")
    zero_count=num_liat.count("0")
    if len(num_liat)==1 or len(num_liat)==2:
        print("0")
    elif one_count==zero_count:
        num_liat.pop()
        one_count=num_liat.count("1")
        zero_count=num_liat.count("0")
        print(min(zero_count,one_count))
    else:
        print(min(zero_count,one_count))