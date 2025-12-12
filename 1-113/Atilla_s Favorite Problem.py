oparations=int(input())
for i in range(oparations):
    input_len=int(input())
    st=input()
    st1=[]
    a_to_z=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for j in range(input_len):
        st1.append(st[j])
    x=max(st1)
    x=a_to_z.index(x)
    print(x+1)