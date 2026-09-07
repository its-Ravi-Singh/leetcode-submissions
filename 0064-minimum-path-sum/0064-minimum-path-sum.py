class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # m, n = len(grid), len(grid[0])
        # dp = [[-1] * (n + 1) for _ in range(m + 1)]
        # def helper(i = m - 1, j = n - 1):
        #     if i == 0 and j == 0: return grid[0][0]
        #     if i < 0 or j < 0: return float('inf')
        #     if dp[i][j] != -1: return dp[i][j]
            
        #     left = helper(i, j-1)
        #     up = helper(i-1, j)

        #     dp[i][j] = min(left, up) + grid[i][j]

        #     return dp[i][j]

        # return helper()

        m, n = len(grid), len(grid[0])
        prev = [0] * n
        prev[0] = grid[0][0]
        for j in range(1, n):
            prev[j] = prev[j-1] + grid[0][j]
        for i in range(1, m):
            temp = [0] * n
            temp[0] = prev[0] + grid[i][0]
            for j in range(1, n):
                temp[j] = min(prev[j], temp[j-1]) + grid[i][j]
            prev = temp

        return prev[-1]