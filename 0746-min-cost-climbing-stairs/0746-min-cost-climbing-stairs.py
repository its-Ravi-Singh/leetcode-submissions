class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n <= 1:
            return cost[n-1]
        
        dp = [-1 for i in range(n+1)]
        dp[0], dp[1] = cost[0], cost[1]

        def helper(n):
            if dp[n] != -1:
                return dp[n]
            
            dp[n] = cost[n] + min(helper(n-1), helper(n-2))
            return dp[n]

        return min(helper(n-1), helper(n-2))