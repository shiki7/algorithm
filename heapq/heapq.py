import heapq

a = [3, 1, 4, 5, 8, 14, 2]

# リストを優先度付きキューに挿入
heapq.heapify(a)

# 最小値の取り出し
print(heapq.heappop(a))

# 最大値を取り出す場合は、＋-反転しておき、取り出した後にもとに戻す)
b = list(map(lambda x: x * (-1), a))
heapq.heapify(b)
print(heapq.heappop(b) * (-1))

# 要素をキューに挿入
heapq.heappush(a, 7)

c = [3, 1, 4, 5, 8, 14, 2]
# 大きい方からn個の取り出す(heapifyの定義は不要)
print(heapq.nlargest(3, c))
# 小さい方からn個の取り出す(heapifyの定義は不要)
print(heapq.nsmallest(3, c))
