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
