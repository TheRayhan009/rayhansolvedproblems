st=input()
low=st.lower()
res1='.'
for i in range(0,len(low)):
    if low[i]!='a' and low[i]!='e' and low[i]!='o' and low[i]!='y' and low[i]!='u' and low[i]!='i' :
        print ("."+ low[i],end="")



# for j in range(0,len(res1)):
#     print('.',end="")
#     print(res1[j])