class Solution:
    def __init__(self):
        self.dp = None

    def uniquePaths(self, i: int, j: int) -> int:
        self.dp = [[-1 for i in range(j + 1)] for i in range(i + 1)]
        return self.helper(i, j)
    
    def helper(self, i: int, j: int) -> int:
        if i == 1 and j == 1: return 1
        if i == 0 or j == 0: return 0
        if self.dp[i][j] != -1: return self.dp[i][j]

        up = self.helper(i-1, j)
        left = self.helper(i, j-1)
        self.dp[i][j] = up + left

        return self.dp[i][j]