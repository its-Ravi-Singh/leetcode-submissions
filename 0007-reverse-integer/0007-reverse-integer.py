class Solution:
    def is_32bit(self, x):
        return -2**31 <= x <= 2**31 - 1
    
    def reverse(self, x: int) -> int:
        ans = int(str(x)[::-1]) if x > 0 else -int(str(abs(x))[::-1])
        return ans if self.is_32bit(ans) else 0