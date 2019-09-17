import itertools

# 3文字の順列、組み合わせを求める
data = [1, 2, 3, 4, 5]
r = 3

# 重複あり順列
print(list(itertools.product(data, repeat=r)))

# 重複なし順列
print(list(itertools.permutations(data, r)))

# 重複あり組み合わせ
print(list(itertools.combinations_with_replacement(data, r)))

# 重複なし組み合わせ
print(list(itertools.combinations(data, r)))
