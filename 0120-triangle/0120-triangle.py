class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1, len(triangle)):
            for j in range(i+1):
                up = triangle[i-1][j] if j < i else float('inf')
                left = triangle[i-1][j-1] if j > 0 else float('inf')
                triangle[i][j] += min(up, left)
        return min(triangle[-1])