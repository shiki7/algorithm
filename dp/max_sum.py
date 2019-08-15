# 最大和問題
def max_sum(N, arr):
    dp = [0] * (N + 1)
    for i in range(N):
        dp[i + 1] = max(dp[i], dp[i] + arr[i])
    return dp[N]


# デバック
if __name__ == "__main__":
    arr = [3, 4, 6, -10, 2, -1, 7, 11]
    N = len(arr)
    print("input: ", arr)
    ans = max_sum(N, arr)
    print("最大合計: ", ans)
