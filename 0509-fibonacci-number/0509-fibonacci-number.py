class Solution:
    def fib(self, n: int, dp: list = []) -> int:
        # DP Memoization Method
        if not dp:
            dp = [-1 for i in range(n+1)]
        
        if n <= 1:
            return n

        if dp[n] != -1:
            return dp[n]
        
        dp[n] = self.fib(n-1, dp) + self.fib(n-2, dp)
        return dp[n]