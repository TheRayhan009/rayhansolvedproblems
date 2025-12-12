st_len=int(input())
st=input()
st=list(st)
ans=[]
num_of_z=st.count("z")
num_of_e=st.count("e")
num_of_r=st.count("r")
num_of_o=st.count("o")
num_of_n=st.count("n")
while True:
    if num_of_o>0 and num_of_n>0 and num_of_e>0:
        ans.append("1")
        num_of_o-=1
        num_of_e-=1
        num_of_n-=1
    if num_of_z>0 and num_of_e>0 and num_of_r>0 and num_of_o>0:
        ans.append("0")
        num_of_z-=1
        num_of_e-=1
        num_of_r-=1
        num_of_o-=1
    else:
        break
print(*ans,sep=" ")