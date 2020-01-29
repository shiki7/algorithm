# BFSで最長距離を求める
# 「.」が通れる。「#」が通れない


from collections import deque
import numpy as np
h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# sy,sx スタート位置
def bfs(sy, sx):
    if s[sy][sx] == '#':
        return -1
    # 未探索ステータス-1で初期化しておく
    dist = [[-1] * w for _ in range(h)]
    dist[sy][sx] = 0
    dq = deque()
    dq.append((sy, sx))
    while dq:
        y, x = dq.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < h and 0 <= nx < w:
                if s[ny][nx] == '#' or dist[ny][nx] != -1:
                    continue
                dist[ny][nx] = dist[y][x] + 1
                dq.append((ny, nx))
    return np.array(dist).max()


ans = 0
for i in range(h):
    for j in range(w):
        ans = max(ans, bfs(i, j))
print(ans)
