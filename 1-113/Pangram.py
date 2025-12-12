ls = int(input())
l = input().lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"
ans = 0

for char in alphabet:
    if char in l:
        ans += 1

if ans == 26:
    print("YES")
else:
    print("NO")
print()