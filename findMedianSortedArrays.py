# Leetcode Question 4

import sys
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.append(sys.maxsize)
        nums2.append(sys.maxsize)
        total = len(nums1) + len(nums2) - 2
        n = int((len(nums1) + len(nums2) - 2)/2) + 1
        merged_array = []
        i = 0
        j = 0
        while True:
            if len(merged_array) == n:
                break
            else:
                if nums1[i] < nums2[j]:
                    merged_array.append(nums1[i])
                    i += 1
                else:
                    merged_array.append(nums2[j])
                    j += 1
        if total % 2 == 0:
            return (merged_array[len(merged_array)-1] + merged_array[len(merged_array)-2])/2
        else:
            return merged_array[len(merged_array)-1]