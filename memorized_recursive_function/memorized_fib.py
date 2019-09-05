# メモ化フィボナッチ関数
def fib_memo(n):
    memo = [0]*(n+1)

    def _fib(n):
        if n <= 1:
            return n
        if memo[n] != 0:
            return memo[n]
        memo[n] = _fib(n-1) + _fib(n-2)
        return memo[n]
        
    return _fib(n)
