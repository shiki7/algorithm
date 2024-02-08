# 10進数をn進数に変換
def base10_to_n(x, n):
    out = ''
    while x > 0:
        out = str(x % n) + out
        x = int(x / n)
    return out

# debug
if __name__ == "__main__":
    x10 = 100
    x5 = base10_to_n(x10, 5)
    print(x5)
