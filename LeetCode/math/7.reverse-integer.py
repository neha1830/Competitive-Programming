#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        pos = x > 0
        res = 0
        if x < 0:
            x = -x
        x = str(x)
        res = int(x[::-1])
        if not pos:
            res = -res
        return 0 if res > pow(2,31) or res < pow(-2,31) else min(res,pow(2,31))
    # @lc code=end

