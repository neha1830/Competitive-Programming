#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")":"(", "}":"{","]":"["}
        for i in s:
            if i in mapping:
                top = stack.pop() if stack else "#"
            
                if mapping[i] != top:
                    return False
            else:
                stack.append(i)
            
        return not stack
# @lc code=end

