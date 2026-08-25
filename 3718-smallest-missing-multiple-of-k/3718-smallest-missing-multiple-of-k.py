class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums = set(nums)
        mult = k
        while True:
            if mult not in nums:
                return mult
            mult += k
