#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        ans = min(strs, key=len)
        final = ans
        for i in strs:
            if i == ans:
                continue
            res = ""
            for k in range(len(ans)):
                if ans[k] != i[k]:
                    break
                if ans[k] == i[k]:
                    res += i[k] 
            if res == "":
                return ""
            if len(res) < len(final):
                final = res
        return final

        #Alternate Solution
        # l = list(zip(*strs))
        # res =""
        # for i in l:
        #     if len(set(i)) == 1:
        #         res += i[0]
        #     else:
        #         break
        # return res
# @lc code=end

