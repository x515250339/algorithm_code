# 给你一个字符串 s，找到 s 中最长的回文子串。
#
#
#
#  示例 1：
#
#
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
#
#
#  示例 2：
#
#
# 输入：s = "cbbd"
# 输出："bb"
#
#
#
#
#  提示：
#
#
#  1 <= s.length <= 1000
#  s 仅由数字和英文字母组成
#
#  Related Topics 字符串 动态规划 👍 5547 👎 0


class Solution:
    def longestPalindrome(self, s: str) -> str:
        d = {}
        m = ""
        l = 0
        for i, v in enumerate(s):
            while v in d.values():
                m += d.pop(l)
                l += 1
            else:
                m += v
            d[i] = v
        return m


print(Solution().longestPalindrome("babad"))
