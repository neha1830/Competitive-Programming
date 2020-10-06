#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        d = {"M" : 1000, "D" : 500, "C" : 100, "L":50, "X" : 10,"V" : 5, "I" : 1}
        i = 0
        while i < len(s) - 1:
            if d[s[i]] < d[s[i+1]]:
                ans += d[s[i+1]] - d[s[i]]
                i += 2
            else:
                ans += d[s[i]]
                i += 1
        if i == len(s) - 1:
            ans += d[s[i]]
        return ans
# @lc code=end

