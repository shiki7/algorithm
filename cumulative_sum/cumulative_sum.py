# 累積和
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ans = [sum(input_list[:i + 1]) for i in range(len(input_list))]
print(ans)

# 上記の場合にTLEする場合は以下を使う
import itertools
ans = list(itertools.accumulate(input_list))
