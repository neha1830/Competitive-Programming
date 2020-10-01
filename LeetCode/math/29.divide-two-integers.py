#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        pos = (divisor < 0) is (dividend < 0)
        dividend,divisor = abs(dividend), abs(divisor)
        ans = 0
        sums = divisor
        while(sums <= dividend):
            quot = 1
            while(sums + sums) <= dividend:
                sums += sums
                quot += quot
            dividend -= sums
            ans += quot
            sums = divisor
        if not pos:
            ans = -ans
        return min(max(-2**31, ans),2**31 -1)
    
        
# @lc code=end

