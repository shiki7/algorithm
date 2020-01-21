# そのまま代入したときの値が変わる副作用を防ぐ
from copy import deepcopy

A = [1,2,3]
B = deepcopy(A)
B[1] = 100
print(A)　
