# ABC079D

def warshall_floyd(d, n):
    # d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d

H, W = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(10)]
a = [list(map(int, input().split())) for _ in range(H)]
n = 10

d = warshall_floyd(c, n)

ans = 0
for i in range(H):
    for j in range(W):
        s = a[i][j]
        if s == 1 or s == -1:
            continue
        ans += d[s][1]
print(ans)
