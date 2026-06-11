class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        def rob2(start, end):
            prev2, prev, cur = 0,0,0
            for i in range(start, end):
                cur = max(prev2+nums[i], prev)
                prev2 = prev
                prev = cur
            return cur
        
        if n == 0: return 0
        elif n == 1: return nums[-1]
        else: return max(rob2(0, n-1), rob2(1, n))