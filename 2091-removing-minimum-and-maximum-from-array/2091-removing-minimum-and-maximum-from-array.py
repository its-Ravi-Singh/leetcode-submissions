class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        a = nums.index(min(nums))
        b = nums.index(max(nums))
        left_ele = min(a, b) + 1
        right_ele = max(a, b) + 1
        n = len(nums)
        # print(left_ele, right_ele, n)
        # 1. removing from both side
        if left_ele == right_ele:
            return left_ele
        both_dis = left_ele + n - right_ele + 1
        left_dis = right_ele
        right_dis = n - left_ele + 1
        # print(both_dis, left_dis, right_dis)
        return min(both_dis, left_dis, right_dis)