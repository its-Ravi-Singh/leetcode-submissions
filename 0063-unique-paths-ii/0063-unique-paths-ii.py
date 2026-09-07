class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        a, b = len(obstacleGrid), len(obstacleGrid[0])
        prev = [0] * b
        for i in range(a):
            temp = [0] * b
            for j in range(b):
                if i == 0 and j == 0 and obstacleGrid[i][j] != 1: temp[0] = 1
                else:
                    if obstacleGrid[i][j] == 1: temp[j] = 0
                    else: temp[j] = (prev[j] if i > 0 else 0) + (temp[j-1] if j > 0 else 0)
            prev = temp
        return prev[b-1]