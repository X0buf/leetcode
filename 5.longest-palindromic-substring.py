# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     5.longest-palindromic-substring
   Description :
   Author :       expbuf
   date：         2020-07-24-15-46
-------------------------------------------------
   Change Activity:
                   2020-07-24-15-46
-------------------------------------------------
"""
__author__ = 'expbuf'


# 动态规划
class Solution:
    # def longestPalindrome(self, s: str) -> str:
    def longestPalindrome(self, s) -> str:
        length = len(s)
        dp = [[0] * length for _ in range(length)]
        # print(dp)
        left, right = 0, 0  # 长度为1时
        for i in range(1, length):
            print(i)
            print(s[i])
            for j in range(length - i):
                print(j)
                print(s[j])
                if s[j] == s[j + i] and (j + 1 >= j + i - 1 or dp[j + 1][j + i - 1]):
                    dp[j][j + i] = 1
                    left, right = j, j + i
                print(dp)
                print(s[left: right + 1])
                print("==========")
        return s[left: right + 1]


# 暴力搜索
class Solution1:
    # 暴力匹配（超时）
    def longestPalindrome(self, s: str) -> str:
        # 特判
        size = len(s)
        if size < 2:
            return s

        max_len = 1
        res = s[0]

        # 枚举所有长度大于等于 2 的子串
        for i in range(size - 1):
            for j in range(i + 1, size):
                if j - i + 1 > max_len and self.__valid(s, i, j):
                    max_len = j - i + 1
                    res = s[i:j + 1]
                    # print(res)
            print(res)
        # return res

    def __valid(self, s, left, right):
        # 验证子串 s[left, right] 是否为回文串
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
            # print(s[left:right])
        return True


# 中心扩展
class Solution2:
    # def longestPalindrome(self, s: str) -> str:
    def longestPalindrome(self, s) -> str:
        length = len(s)
        dp = [[0] * length for _ in range(length)]
        # print(dp)
        left, right = 0, 0  # 长度为1时
        for i in range(1, length):
            print(i)
            print(s[i])
            for j in range(length - i):
                print(j)
                print(s[j])
                if s[j] == s[j + i] and (j + 1 >= j + i - 1 or dp[j + 1][j + i - 1]):
                    dp[j][j + i] = 1
                    left, right = j, j + i
                print(dp)
                print(s[left: right + 1])
                print("==========")
        return s[left: right + 1]


class Solution3:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size < 2:
            return s

        dp = [[False for _ in range(size)] for _ in range(size)]
        # print(dp)
        max_len = 1
        start = 0

        for i in range(size):
            dp[i][i] = True
            # print(dp)

        for j in range(1, size):
            for i in range(0, j):
                print(i)
                print(j)
                print("=====")
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False

                if dp[i][j]:
                    cur_len = j - i + 1
                    if cur_len > max_len:
                        max_len = cur_len
                        start = i
                        # print(start, start + max_len)
            print(s[start:start + max_len])
        return s[start:start + max_len]


def test():
    a = [1]
    cnt = len(a)
    for i in range(0, cnt):
        print(i)


if __name__ == '__main__':
    s = Solution()
    # s = Solution1()
    # s = Solution2()
    # s = Solution3()
    a = "babad"
    # a = "aa"
    a = s.longestPalindrome(a)
    # print(a)
    # test()
    # print(s.longestPalindrome.__annotations__)
    # print(s.longestPalindrome("test"))
    # print(longestPalindrome("123", "test"))
