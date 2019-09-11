# 部分和
# 整数 a1, a2,....anの和をkにできるかを判定
# 4
# 1 2 4 7
# 13
n = int(input())
a = list(map(int, input().split()))
k = int(input())


def dfs(i, total):
    if i == n:
        return total == k
    # a[i]を使う場合
    if dfs(i+1, total + a[i]):
        return True
    # a[i]を使わない場合
    if dfs(i+1, total):
        return True
    # kが作れない場合
    return False


if dfs(0, 0):
    print('Yes')
else:
    print('No')
