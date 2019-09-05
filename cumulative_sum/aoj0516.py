# K連続する最大値の組み合わせを求める
K = 3
a = [2, 5, -4, 10, 3, 5, -4, 1]

# K連続の累積和のリスト
c = [sum(a[i:i + K]) for i in range(len(a) - K + 1)]

c_index = c.index(max(c))
print(a[c_index:c_index + K])
