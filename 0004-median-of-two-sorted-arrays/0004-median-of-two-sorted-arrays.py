class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = len(nums1) + len(nums2)
        total = sorted(nums1+nums2)
        if a % 2 == 0:
            return (total[a//2] + total[(a//2)-1])/2
        else:
            return total[a//2]