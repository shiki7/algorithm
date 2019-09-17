# しゃくとり法
# sの積がK以下になる最大の長さを求める
N, K = map(int, input().split())
s = [int(input()) for _ in range(N)]
left = 0
right = 1
ans = 0
total = s[0]
if 0 in s:
    print(N)
    exit()

while right < N:
    # 上限に達していない場合、右端を進める
    if total * s[right] <= K:
        total *= s[right]
        right += 1
        ans = max(ans, right - left)
    # 一つの数字で上限を超えている場合、右端、左端を進める
    elif right == left:
        right += 1
        left += 1
    # 上限を超えている場合、左端を進める
    else:
        total //= s[left]
        left += 1
print(ans)
