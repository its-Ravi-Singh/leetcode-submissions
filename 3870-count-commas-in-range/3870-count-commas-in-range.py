import math
class Solution:
    def countCommas(self, n: int) -> int:
        return n-999 if math.log10(n) >= 3 else 0