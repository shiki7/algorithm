# K連続する最大値の組み合わせを求める
K = 3
a = [2, 5, -4, 10, 3, 5, -4, 1]

# 累積和
c = [sum(a[:i + 1]) for i in range(len(a) - K + 1)]

ans = []
for i in range(len(c)-K):
    ans.append(c[i+K] - c[i])
print(max(ans))
