# code-festival-2017-qualb/B
from collections import Counter

n = int(input())
d = list(map(int, input().split()))
m = int(input())
t = list(map(int, input().split()))

counter1 = Counter(d)
counter2 = Counter(t)

for k, v in counter2.items():
    if counter1[k] < v:
        print('NO')
        exit()
print('YES')
