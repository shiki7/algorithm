# 浮動小数点で誤差が出ないようにするための計算
from decimal import Decimal
a, b = map(Decimal, input().split())
print(int(a*b))
