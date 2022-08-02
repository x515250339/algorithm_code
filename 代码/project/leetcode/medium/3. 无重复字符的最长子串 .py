# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
#
#
#
#  示例 1:
#
#
# 输入: s = "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#
#
#  示例 2:
#
#
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#
#
#  示例 3:
#
#
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#
#
#
#
#  提示：
#
#
#  0 <= s.length <= 5 * 10⁴
#  s 由英文字母、数字、符号和空格组成
#
#
#  Related Topics 哈希表 字符串 滑动窗口 👍 7902 👎 0


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = set()
        ma, su, left = 0, 0, 0
        for i in range(len(s)):
            su += 1
            while s[i] in d:
                d.remove(s[left])
                left += 1
                su -= 1
            d.add(s[i])
            ma = max(ma, su)
        return ma


print(Solution().lengthOfLongestSubstring("abcabcbb"))
# print(Solution().lengthOfLongestSubstring("pwwkew"))
# print(Solution().lengthOfLongestSubstring(" "))
# print(Solution().lengthOfLongestSubstring("aa"))
# print(Solution().lengthOfLongestSubstring("abcb"))
# print(Solution().lengthOfLongestSubstring("dvdf"))
# print(Solution().lengthOfLongestSubstring("pwwkew"))
