first_guest_name=input()
second_guest_name=input()
shuffleded=list(str(input()))
ans=0
shuffleded.sort()
for i in range(len(first_guest_name)):
    if first_guest_name[i] in shuffleded:
        ans = ans + 1
        shuffleded.remove(first_guest_name[i])
for j in range(len(second_guest_name)):
    if second_guest_name[j] in shuffleded:
        ans = ans + 1
        shuffleded.remove(second_guest_name[j])
x=len(first_guest_name)+len(second_guest_name)
if len(shuffleded)==0 and x==ans:
    print("YES")
else:
    print("NO")