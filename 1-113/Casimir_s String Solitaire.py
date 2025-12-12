oparations=int(input())
for i in range(oparations):
    s=1
    st=input()
    if len(st)%2!=0:
        print("NO")
    else:
        a=st.count("A")
        b=st.count("B")
        c=st.count("C")
        if a+c==b:
            print("YES")
        else:
            print("NO")


#-------------------------------------------------------------------------------------------------------



# oparations=int(input())
# for i in range(oparations):
#     s=1
#     st=input()
#     if len(st)%2!=0:
#         print("NO")
#     else:
#         string=[]
#         ans=0
#         for j in range(0,len(st)-1,2):
#             v=st[j]+st[j+1]
#             string.append(v)
#         lenx=len(string)
#         for x in range(0,lenx):
#             if string[0]=="AB" or string[0]=="BA":
#                 string.remove(string[0])
#                 ans=ans+1
#             elif string[0]=="CB" or string[0]=="BC":
#                 string.remove(string[0])
#                 ans=ans+1
#             x=x+1
#         g=''.join(string)
#         for k in range(0,len(g)-1):
#             if g[k]+g[k+1]=="AB" or g[k]+g[k+1]=="BA" or g[k]+g[k+1]=="CB" or g[k]+g[k+1]=="BC":
#                 ans=ans+1    
#         if ans==lenx:
#             print("YES")
#         else:
#             print("NO")



#----------------------------------------------------------------------

# oparations=int(input())
# for i in range(oparations):
#     x=0
#     s=1
#     st=input()
#     if len(st)%2!=0:
#         print("NO")
#     else:
#         string=[]
#         for j in range(0,len(st)-1,2):
#             v=st[j]+st[j+1]
#             string.append(v)
#         while x<len(string)+1:
#             if string[0]=="AB" or string[0]=="BA":
#                 string.remove(string[0])
#             elif string[0]=="CB" or string[0]=="BC":
#                 string.remove(string[0])
#             else:
#                 s=0
#                 print("NO")
#                 break
#             x=x+1
#         if s==1:
#             string=''.join(string)
#             print(string)
#             if len(string)==0:
#                 print("YES")
#             else:
#                 print("NO")