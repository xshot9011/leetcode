# https://leetcode.com/problems/median-of-two-sorted-arrays/
# TBH, cannot figure out log(m+n) solution 
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        median = 0
        sortNum = nums1 + nums2
        sortNum.sort()
        isHole = len(sortNum) % 2 == 0

        if isHole:
            median = (sortNum[(len(sortNum) // 2) - 1] + sortNum[(len(sortNum) // 2)])/2
        else:
            median = sortNum[(len(sortNum) // 2)]
        # Time: O(k) + O(nums1+nums2(log(nums1+nums2))) = O((nums1+nums2)log(nums1+nums2))
        # Space: O(nums1+nums2)
        return median

    def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float:
        median = 0
        sortNum = []
        pointer1 = 0
        pointer2 = 0
        counter = 0
        isHole = (len(nums1)+len(nums2)) % 2 == 0
        maxCounter = ((len(nums1)+len(nums2)) // 2) + 1

        while pointer1 < len(nums1) and pointer2 < len(nums2) and counter < maxCounter:
            if nums1[pointer1] < nums2[pointer2]:
                sortNum.append(nums1[pointer1])
                pointer1 += 1
            else:
                sortNum.append(nums2[pointer2])
                pointer2 += 1
            counter += 1
        
        while counter < maxCounter:
            if pointer1 == len(nums1):
                sortNum.append(nums2[pointer2])
                pointer2 += 1
            elif pointer2 == len(nums2):
                sortNum.append(nums1[pointer1])
                pointer1 += 1

            counter += 1
        
        if isHole:
            median = (sortNum[-1]+sortNum[-2])/2
        else:
            median = sortNum[-1]
        # Time: O((m+n)/2) + O((m+n)/2) = O(m+n)
        # Space: O((m+n)/2) = O(m+n)
        return median
