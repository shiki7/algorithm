# 累積和
from itertools import accumulate

A = [1,4,3,4,6,5]
print(list(accumulate(A))) #[1, 5, 8, 12, 18, 23]
