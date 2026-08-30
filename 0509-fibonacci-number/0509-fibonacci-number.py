class Solution:
    def fib(self, n: int, prev1: int = 1, prev2: int = 0) -> int:
        # DP Memoization Method more optimise with only 2 var
        if n <= 1: return n
        for i in range(2, n+1):
            prev1, prev2 = prev1 + prev2, prev1
        return prev1