# 滞在する必要のあるノードは１つ。最短経路で到達、滞在、戻る。
# max( (与えられた時間 - 到達時間 - 戻る時間) * 報酬)
# 負数がないので、ダイクストラでそれぞれの頂点の最短時間を求める

from heapq import heappush, heappop

# ダイクストラ（ヒープキューで高速化）
def dijkstra(start, n, edge):
    # 始点sから各頂点への最短距離を求める
    # n:頂点数
    # d:各頂点へのコスト(存在しないときはinf)
    # q:キュー(スタートからのコスト,頂点)
    # edge[i] : (iから頂点までのコスト, 頂点のindex）
    d = [float("inf")] * n
    d[start] = 0
    # スタートをキュー(cost, 頂点のindex)に入れる
    q = [(0, start)]

    while len(q) != 0:
        # キューの先頭を取得
        cost_i, i = heappop(q)
        if d[i] < cost_i:
            continue

        # キューの先頭から繋がっている頂点を探索
        for cost_j, j in edge[i]:
            if d[j] > d[i] + cost_j:
                d[j] = d[i] + cost_j
                heappush(q, (d[j], j))
    return d

# input
N, M, T = map(int, input().split())
A = list(map(int, input().split()))
edge1 = [[] for _ in [0]*N]
edge2 = [[] for _ in [0]*N]
for _ in range(M):
    a, b, c = (int(x) for x in input().split())
    # 往復するため両方向定義(片方向なら一つで良い）
    edge1[a-1].append((c, b-1))
    edge2[b-1].append((c, a-1))

go = dijkstra(0, N, edge1)
prev = dijkstra(0, N, edge2)

ans = 0
for v in range(N):
    remain = T - (go[v] + prev[v])
    ans = max(ans, remain * A[v])
print(int(ans))
