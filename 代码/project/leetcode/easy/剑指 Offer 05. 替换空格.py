class Solution:
    def replaceSpace(self, s: str) -> str:
        """
        手写硬撸 python内置方法
        :param s:
        :return:
        """
        # return s.replace(" ", "%20")
        return "%20".join(s.split(" "))


class Solution:
    def replaceSpace(self, s: str) -> str:
        """
        手写硬撸 python内置方法
        :param s:
        :return:
        """
        s = list(s)
        for i, v in enumerate(s):
            if v == " ":
                s[i] = "%20"
        return "".join(s)


class Solution:
    def replaceSpace(self, s: str) -> str:
        res = ''
        for c in s:
            if c == ' ':
                res += '%20'
            else:
                res += c
        return res


s = "We are happy."
print(Solution().replaceSpace(s))
