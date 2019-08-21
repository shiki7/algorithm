# ユークリッド互除法
# 自然数 𝑎,𝑏(𝑎≥𝑏) に対し 𝑎 を 𝑏 で割ったあまりを 𝑟 とすると、次の式が成り立つ。
# 𝑔𝑐𝑑(𝑎,𝑏)=𝑔𝑐𝑑(𝑏,𝑟)

def gcd(a, b):
    if a < b:
        a, b = b, a
    while a % b != 0:
        a, b = b, a % b
        return b

a, b = map(int, input().split())
print(gcd(a, b))
