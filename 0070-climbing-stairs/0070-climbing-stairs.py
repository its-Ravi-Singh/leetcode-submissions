class Solution:
    def climbStairs(self, n: int, dp: list = []) -> int:
        if not dp:
            dp = [-1 for i in range(n+1)]
        if dp[n] != -1:
            return dp[n]
        if n <= 1:
            return 1
        dp[n] = self.climbStairs(n-1, dp) + self.climbStairs(n-2, dp)
        return dp[n]