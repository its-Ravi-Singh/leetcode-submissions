from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data = defaultdict(list)
        for i, num in enumerate(nums):
            if num in data:
                return [data[num], i]
            data[target - num] = i