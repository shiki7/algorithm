# ナップサック問題
# N個の荷物の重さがW以下になるように詰め込むときの価値の最大化
# weight:重さ　　value:価値


def knapsack(N, W, weight, value):
    # 初期化
    inf = float("inf")
    dp = [[-inf for i in range(W + 1)] for j in range(N + 1)]
    for i in range(W + 1):
        dp[0][i] = 0

    # DP
    for i in range(N):
        for w in range(W + 1):
            if weight[i] <= w:  # dp[i][w-weight[i]の状態にi番目の荷物が入る可能性がある
                dp[i + 1][w] = max(dp[i][w - weight[i]] + value[i], dp[i][w])
            else:
                dp[i + 1][w] = dp[i][w]
    return dp[N][W]


# デバック
if __name__ == "__main__":
    print(knapsack(4, 400, [50, 100, 150, 200], [30, 70, 95, 120]))
