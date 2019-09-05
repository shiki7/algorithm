# 累積和
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ans = [sum(input_list[:i + 1]) for i in range(len(input_list))]
print(ans)
