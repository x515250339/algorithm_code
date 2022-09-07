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
    def helper(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        print(s[left + 1: right])
        return s[left + 1: right]

    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            cur1 = self.helper(s, i, i)
            cur2 = self.helper(s, i, i + 1)
            res = cur1 if len(cur1) > len(res) else res
            res = cur2 if len(cur2) > len(res) else res

        return res


print(Solution().longestPalindrome("babad"))
