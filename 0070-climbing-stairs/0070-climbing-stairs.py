class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        prev = prev2 = 1
        for i in range(2, n+1):
            prev, prev2 = prev + prev2, prev
        return prev