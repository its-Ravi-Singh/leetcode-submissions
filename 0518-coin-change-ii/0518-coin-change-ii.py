class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        t = [0 for _ in range(amount+1)]
        t[0] = 1
        for i in range(1, n+1):
            for j in range(coins[i-1], amount+1):
                if(coins[i-1] <= j):
                    t[j] = t[j] + t[j-coins[i-1]]
        return t[-1]