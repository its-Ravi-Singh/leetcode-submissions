import math
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        a = n
        nums = []
        while n > 0:
            nums.append(n%10)
            n //= 10
        num_sum = sum(nums)
        num_prod = math.prod(nums)
        if a % (num_sum + num_prod) == 0:
            return True
        return False