import math
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        a = n
        nums = []
        num_prod = 1
        num_sum = 0
        while n > 0:
            r = n%10
            nums.append(r)
            n //= 10
            num_prod *= r
            num_sum += r
        if a % (num_sum + num_prod) == 0:
            return True
        return False