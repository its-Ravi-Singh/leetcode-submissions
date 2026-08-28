import math
class Solution:
    def countDigits(self, num: int) -> int:
        val = 0
        num_check = num
        while num > 0:
            if num_check % (num % 10) == 0:
                # print(num % 10)
                val += 1
            num //= 10
        print(val)
        return val