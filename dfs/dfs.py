def dfs(pos, ~~~):
    # 停止条件
    # 深さに限らず，任意の停止条件を書く
    if pos == N: 
        return ~~~

    # pos を進めながら（末端に進みながら）分岐処理
    # 末端まで到達した時それぞれの分岐から値が返される
    # for 文で書ける場合は for 文で実装
    ret1 = dfs(pos + 1, 分岐 1)
    ret2 = dfs(pos + 1, 分岐 2)
    ret3 = dfs(pos + 1, 分岐 3)
    ret4 = dfs(pos + 1, 分岐 4)
    

    # それぞれの分岐からの戻り値の処理を行う関数
    return func(ret1, ret2, ret3, ret4)
