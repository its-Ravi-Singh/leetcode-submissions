import math
class Solution:
    def countDigits(self, num: int) -> int:
        val = 0
        num_check = num
        while num > 0:
            if num_check % (num % 10) == 0:
                val += 1
            num //= 10
        return val