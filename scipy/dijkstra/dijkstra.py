# ABC035D

# scipyのダイクストラ法で解く
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix

N, M, T = map(int, input().split())
A = list(map(int, input().split()))
start, goal, cost = [], [], []
for _ in range(M):
    a, b, c = map(int, input().split())
    # 行き帰りで両方定義
    start.append(a-1)
    goal.append(b-1)
    cost.append(c)

# csr_matrix形式にしないとTLEになるので必ず変換する。
d1 = csr_matrix((cost, (start, goal)), shape=(N, N))
d2 = csr_matrix((cost, (goal, start)), shape=(N, N))

# 始点,終点は0のみなのでindicesを指定
d1 = dijkstra(d1, indices=0)
d2 = dijkstra(d2, indices=0)
ans = 0
for i in range(N):
    remain = T - (d1[i] + d2[i])
    ans = max(ans, remain * A[i])
print(int(ans))
