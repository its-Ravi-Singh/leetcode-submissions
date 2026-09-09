class Solution:
    def countCommas(self, n: int) -> int:
        p, count = 1000, 0
        while p <= n:
            count += n - p + 1
            p *= 1000
        return count