data = [1, 2, 3, 4]

ans = []
for d in data:
    if d % 2 == 0:
        ans.append(d * 2)
print(ans)

# リスト内包型
ans = [d * 2 for d in data if d % 2 == 0]
print(ans)

# ラムダ型
tmp = list(filter(lambda x: x % 2 == 0, data))
ans = list(map(lambda x: x * 2, tmp))
print(ans)

# 複数のリストを同時に展開する
A = ['x', 'y', 'z']
B = [10, 20, 30]
for a, b in zip(A, B):
    print(a, b)

    
#  2次元配列(print結果は同じだが、bのように書かないと代入した際に副作用が出る）
a = [[0]*n]*n
b = [[0 for _ in range(n)] for _ in range(n)]
