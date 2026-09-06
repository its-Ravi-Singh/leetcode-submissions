class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        def helper(start, end):
            prev2 = prev = 0
            for i in range(start, end):
                prev2, prev = prev, max(prev2+nums[i], prev)
            return prev
        
        if n == 0: return 0
        if n <= 3: return max(nums)
        return max(helper(0, n-1), helper(1, n))