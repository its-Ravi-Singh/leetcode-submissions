class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        prev2 = prev = 0
        for i in range(0, n):
            prev2, prev = prev, max(prev2 + nums[i], prev)
        return prev