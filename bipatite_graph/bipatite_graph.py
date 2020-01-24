# 二部グラフの判定

# n: 頂点の数
# m: 辺の数
# a,b: 頂点aからbに辺がある
# dd: 辺のつながりを格納する辞書
# color: 色(1,-1)

from collections import defaultdict

n, m = map(int, input().split())

dd = defaultdict(set)
for i in range(m):
    a, b = list(map(int, input().split()))
    dd[a].add(b)
    dd[b].add(a)

color = [0 for i in range(n+1)]


def dfs(u, v, searched=[]):

    # u: 現在の頂点
    # v: 参照する頂点
    global color
    searched.append(u)

    for i in list(dd[u]):
        if color[i] == v:
            return False
        elif i not in searched:  # 未探索の場合は再起
            color[i] = v*(-1)  # 1,-1を交互に色分ける
            dfs(i, -v, searched)
    return True


color[1] = 1  # 始点を塗る
if dfs(1, 1):
    print('Yes')
else:
    print('No')
