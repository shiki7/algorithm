# いもす法

# 区間指定で何度もカウンティングする問題を解く
# lからrまでのインクリメントを繰り返す場合に、
# 1. a[l-1]をインクリメント、a[r]をデクリメントをQ回繰り返す
# 2. 1の累積和を取る

import itertools

# 入力
N, Q = map(int, input().split())
lr = [list(map(int, input().split())) for _ in range(Q)]

a = [0] * (N+1)

for i in range(Q):
    le = lr[i][0]
    ri = lr[i][1]
    a[le-1] += 1
    a[ri] -= 1

# 累積和
b = list(itertools.accumulate(a))
