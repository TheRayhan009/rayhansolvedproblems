t = int(input())

for _ in range(t):
    a, b, r = map(int, input().split())

    max_xor = a ^ b
    result = min(max_xor, r)

    if max_xor > r:
        bit_position = max_xor.bit_length() - 1
        mask = (1 << bit_position) - 1
        result = min(result, max_xor & ~mask)

    print(result)
