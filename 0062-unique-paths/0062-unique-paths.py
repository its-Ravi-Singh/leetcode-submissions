class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0] * n
        for i in range(m):
            temp = [0] * n
            for j in range(n):
                if i == 0 and j == 0: temp[0] = 1
                else:
                    temp[j] = (dp[j] if i > 0 else 0) + (temp[j-1] if j > 0 else 0)
            dp = temp
        return dp[n-1]