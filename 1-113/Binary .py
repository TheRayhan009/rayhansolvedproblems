from ctypes import c_longlong as ll
while True:
    print("FOR STRING TO BINARY PRESS 1 AND FOR BINARY TO STRING PRESS 2")
    print("-->",end="")
    want=int(input())
    if want==1:
        print("ENTER YOUR STRING.")
        print("-->",end="")
        st=input()
        for i in range(len(st)):
            res = ''.join(format(ord(i), '08b') for i in st[i])
            print(res,end="")
        print("\n")     
    elif want==2:
        print("ENTER YOUR BINARY NUMBER.")
        print("-->",end="")
        st=input()
        str = ""
        for i in range(0, len(st), 8):
            binc = st[i:i + 8]
            num = int(binc, 2)
            str += chr(num)
        print(str,"\n")
    else:
        print("ops!! TRY AGAIN")