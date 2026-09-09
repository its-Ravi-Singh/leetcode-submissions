class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = sorted(nums1+nums2)
        a = len(total)
        mid = a // 2
        if a % 2 == 0:
            return (total[mid] + total[mid-1])/2
        else:
            return total[mid]