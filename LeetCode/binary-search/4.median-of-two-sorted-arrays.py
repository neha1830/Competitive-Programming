#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = a = len(nums1) - 1
        n = b = len(nums2) - 1
        cnt = m + n + 1
        for _ in range(n + 1):
            nums1.append(0)
        while m >= 0 and n >= 0:
            if nums1[m] <= nums2[n]:
                nums1[cnt] = nums2[n]
                n -= 1
                cnt -= 1
            else:
                nums1[cnt] = nums1[m]
                cnt -= 1
                m -= 1
        while n >= 0:
            nums1[cnt] = nums2[n]
            n-= 1
            cnt -= 1
        t = a + b + 2
        if t %2 == 0:
            return (nums1[t//2] + nums1[t//2 - 1])/2  
        return nums1[t//2] 
        
        # @lc code=end

