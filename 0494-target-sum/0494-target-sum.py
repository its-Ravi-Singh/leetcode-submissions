class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if abs(target)>total or (target+total)%2!=0: return 0

        n = len(nums)
        s1 = (total + target) // 2
        t = [[0 for _ in range(s1+1)] for _ in range(n+1)]
        t[0][0] = 1
        for i in range(1, n+1):
            if nums[i-1] == 0:
                t[i][0] = 2 * t[i-1][0]
            else:
                t[i][0] = t[i-1][0]
        for i in range(1, n+1):
            for j in range(1, s1+1):
                val = nums[i-1]
                if(val <= j):
                    t[i][j] = t[i-1][j-val] + t[i-1][j]
                else:
                    t[i][j] = t[i-1][j]
        return(t[n][s1])