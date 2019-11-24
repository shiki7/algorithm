from bisect import bisect_left

nums = [1,2,5,7,10,11, 32]

# ソート済みのリストに新たに値を入れる場合にindexを返してくれる
print(bisect_left(nums, 8))
