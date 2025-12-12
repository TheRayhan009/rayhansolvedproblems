first_len,second_len,third_len,forth_len=map(int,input().split())
cubs=input()
ans=0
for i in range(len(cubs)):
    if cubs[i]=="1":
        ans=ans+first_len
    elif cubs[i]=="2":
        ans=ans+second_len
    elif cubs[i]=="3":
        ans=ans+third_len
    elif cubs[i]=="4":
        ans=ans+forth_len
print(ans)