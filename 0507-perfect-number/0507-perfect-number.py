class Solution:
    def checkPerfectNumber(self, n: int) -> bool:
        arr = [(i, n // i) for i in range(1, int(n ** 0.5) + 1) if n % i == 0]
        return sum(set(sum(arr, ()))) == n * 2