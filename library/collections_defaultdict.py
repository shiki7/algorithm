# dictとは異なり、存在しないキーを参照、代入してもエラーが出ない。（定義時に初期化される）
from collections import defaultdict

A = [int(i) for i in input().split()]
dd = defaultdict(int)
for a in A:
    dd[a]+=1
    
    
# 0を返す
d = defaultdict(lambda: 0)
for key in A:
    d[key] += 1
