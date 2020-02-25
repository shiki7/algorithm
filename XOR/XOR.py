# シフト演算はnumpyのarray型を利用する

import numpy as np

n = int(input())
a = np.array(list(map(int, input().split())))
mod = 10**9+7
 
ans = 0
max_digit = 0
for i in range(n):
    max_digit = max(max_digit, len(bin(a[i])))

# 各桁の2**i * （0の数 * 1の数） の和
for i in range(max_digit):
    num1 = np.count_nonzero((a >> i) & 1)  # 1の数
    num2 = n - num1  # 0の数
    ans += pow(2, i, mod) * (num1 * num2) % mod
print(ans % mod)
