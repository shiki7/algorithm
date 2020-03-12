# ビット演算

money = 300
item = (("みかん", 100), ("りんご", 200), ("ぶどう", 300))
n = len(item)
for i in range(2 ** n):
    bag = []
    print("pattern {}: ".format(i), end="")
    for j in range(n):  # このループが一番のポイント
        if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
            bag.append(item[j][0])  # フラグが立っていたら bag に果物を詰める
    print(bag)

    

# itertoolsを使えば以下のようにも書ける
# 3桁の[0,1]の組み合わせ
import itertools
for i in itertools.product([0, 1], repeat=3):
    print(i)
