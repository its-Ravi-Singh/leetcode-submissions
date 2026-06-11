class Solution:
    def longestCommonSubsequence(self, x: str, y: str) -> int:
        m = len(x)
        n = len(y)
        dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]
        def lcs(x, y, m, n):
            if n == 0 or m == 0:
                return 0
            if dp[m][n] != -1:
                return dp[m][n]
            if x[m-1] == y[n-1]:
                dp[m][n] = 1 + lcs(x, y, m-1, n-1)
                return dp[m][n]
            else:
                dp[m][n] = max(lcs(x, y, m-1, n), lcs(x, y, m, n-1))
                return dp[m][n]
        return lcs(x, y, m, n)