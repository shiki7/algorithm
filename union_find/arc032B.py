def find_root(x):
    if parent[x] == x:
        return x
    else:
        return find_root(parent[x])


def unite(x, y):
    x = find_root(x)
    y = find_root(y)

    if x != y:
        if rank[x] < rank[y]:
            parent[x] = y
            size[y] += size[x]
        else:
            parent[y] = x
            size[x] += size[y]
            if rank[x] == rank[y]:
                rank[x] += 1


def roots():
    roots = []
    for i in range(n):
        roots.append(find_root(i))
    return roots


n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]

parent = [i for i in range(n)]  # 根
rank = [1] * n  # 深さ
size = [1] * n  # iを根とするグループのサイズ

edge = [[ab[m - 1 - i][0] - 1, ab[m - 1 - i][1] - 1] for i in range(m)]

for i in range(m):
    unite(edge[i][0], edge[i][1])
print(len(set(roots()))-1)
