t = int(input())
for _ in range(t):
    s = input().strip()
    digits = sorted(int(ch) for ch in s)
    ans = []
    for i in range(10):
        need = 10 - i - 1
        for j in range(len(digits)):
            if digits[j] >= need:
                ans.append(str(digits[j]))
                digits.pop(j)
                break
    print(''.join(ans))
