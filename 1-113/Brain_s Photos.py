row,colam=map(int,input().split())
ans_num=0
for i in range(row):
    st_list=list(map(str,input().split()))
    if "C" in st_list or "M" in st_list or "Y" in st_list:
        ans_num=1
if ans_num==1:
    print("#Color")
else:
    print("#Black&White")