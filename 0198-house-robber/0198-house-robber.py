class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        prev2, prev, cur = 0, 0, 0
        for i in range(0, n):
            cur = max(prev2 + nums[i], prev)
            prev2 = prev
            prev = cur
        return cur