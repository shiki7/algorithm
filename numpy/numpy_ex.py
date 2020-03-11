import numpy as np

array_zeros = np.zeros((2, 3))
print(array_zeros)
# [[0. 0. 0.]
#  [0. 0. 0.]]

array_ones = np.ones((2, 3))
print(array_ones)
# [[1. 1. 1.]
#  [1. 1. 1.]]

a = np.arange(5)
print(a)
# [0 1 2 3 4]

a = np.arange(1, 5)
print(a)
# [1 2 3 4]

a = np.arange(6).reshape(2, 3)
print(a)
# [[0 1 2]
#  [3 4 5]]

print(a.sum(axis=0))  # 縦軸の和
# [3 5 7]

print(a.sum(axis=1))  # 横軸の和
# [ 3 12]

a = np.arange(6).reshape(3, 2)
a.resize(2, 3)  # reshapeを繰り返すと変更されないのでresizeだと変更される
print(a)
# [[0 1 2]
#  [3 4 5]]

a = np.array([1, 2, 3], dtype=np.int64)
print(a.dtype)
# int64

# #####配列計算####### #
a = np.array([10, 20, 30, 40])
b = np.array([0, 1, 2, 3])
print(a+b)
# [10 21 32 43]

print(b ** 2)
# [0 1 4 9]

print(np.arange(5) ** 2)
# [ 0  1  4  9 16]

a = np.arange(12).reshape(2, 3, 2)
print(np.max(a))  # 多次元配列の中の最大値
# 11

a = np.arange(10).reshape(2, 5)
print(np.argmax(a))  # 最大値のindex(1次元でカウントされる)
# 9

a = np.arange(6).reshape(2, 3)
print(a.ravel())  # 1次元配列に変換
# [0 1 2 3 4 5]

a = np.arange(6).reshape(2, 3)
print(a > 3)  # 比較
# [[False False False]
#  [False  True  True]]

a = np.arange(6).reshape(2, 3)
print(np.zeros_like(a))  # 同じ形状の0行列を返す。 onesもある
# [[0 0 0]
#  [0 0 0]]

print(np.random.rand(3))  # ランダムな値の入った配列
# ex) [0.45703208 0.52284898 0.38695055]

print(np.random.randint(0, 100, 10))  # 0から100を10個生成
# ex) [56 60 81 20 35 79 71 63 77 60]

a = np.arange(3)
print(np.exp(a))  # 指数関数
# [1.         2.71828183 7.3890561 ]
print(np.log1p(a))  # 対数関数
# [1.         2.71828183 7.3890561 ]
# [0.         0.69314718 1.09861229]


print(np.linspace(0, 15, 4))  # 第３引数個の等差数列
# [ 0.  5. 10. 15.]
print(np.linspace(0, 10, 4, dtype=int))  # 小数点をint型に変換
# [ 0  3  6 10]
print(np.arange(3, 10, 2))  # 第３引数おきの等差数列
# [3 5 7 9]
print(np.geomspace(1, 27, 4))  # 等比数列
# [ 1.  3.  9. 27.]
