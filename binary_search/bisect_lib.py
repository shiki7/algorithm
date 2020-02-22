from bisect import bisect_left

nums = [1,2,5,7,10,11, 32]

# ソート済みのリストに新たに値を入れる場合にindexを返してくれる
print(bisect_left(nums, 8))

# 挿入
A = [1, 2, 3, 3, 3, 4, 4, 6, 6, 6, 6]
insort(A, 3) # [1, 2, 3, 3, 3, 3, 4, 4, 6, 6, 6, 6]
