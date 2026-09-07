class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Initialize first row (can only come from left)
        for j in range(1, n):
            grid[0][j] += grid[0][j-1]
        
        # Fill rest of grid in-place
        for i in range(1, m):
            # First column (can only come from up)
            grid[i][0] += grid[i-1][0]
            
            # Rest of row (min of up or left)
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        
        return grid[m-1][n-1]