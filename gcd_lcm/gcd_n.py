def gcd(a, b):
    if a < b:
        a, b = b, a
    while a % b != 0:
        a, b = b, a % b
    return b


a = list(map(int, input().split()))
ans = a[0]
for i in range(1, len(a)):
    ans = gcd(ans, a[i])
print(ans)
