# union find
def find_root(x):
    if parent[x] == x:
        return x
    else:
        return find_root(parent[x])


def unite(x, y):
    '''x,yの属する集合の併合'''
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


def same(x, y):
    '''xとyが同じグループかどうか判定'''
    return find_root(x) == find_root(y)


def group_size(x):
    '''xが所属するグループのサイズ'''
    return size[find_root(x)]


def roots():
    '''rootリストを返す'''
    roots = []
    for i in range(N):
        roots.append(find_root(i))
    return roots


def group_count():
    '''グループの数'''
    return len(set(roots()))


# 入力
N, M = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(M)]

# 初期化
parent = [i for i in range(N)]  # 根
rank = [1] * N  # 深さ
size = [1] * N  # iを根とするグループのサイズ

# 前処理 (問題によって、適宜変える）
edge = [[ab[M - 1 - i][0] - 1, ab[M - 1 - i][1] - 1] for i in range(M)]

# 結合
for i in range(M):
    unite(edge[i][0], edge[i][1])



# 出力（問題によって適宜変える）

