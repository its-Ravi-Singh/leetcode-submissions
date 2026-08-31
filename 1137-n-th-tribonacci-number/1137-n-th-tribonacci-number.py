class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        if n == 2:
            return 1
        first = 0
        second = 1
        third = 1
        for i in range(3, n+1):
            first, second, third = second, third, (first + second + third)
        return third