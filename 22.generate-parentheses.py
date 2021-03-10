# -*- coding: utf-8 -*-
"""
   @FileName :   22.generate-parentheses.py
   @Email :      expbuf@hotmail.com
   @Date :       2021/03/09 21:11
   @Author :     expbuf
   @Description :
"""
__author__ = 'expbuf'

"""

数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

示例 1：
    输入：n = 3
    输出：["((()))","(()())","(())()","()(())","()()()"]
示例 2：
    输入：n = 1
    输出：["()"]

提示：
    1 <= n <= 8

回溯算法（深度优先遍历）+ 广度优先遍历
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        cur_str = ''

        def dfs(cur_str, left, right):
            """
            :param cur_str: 从根结点到叶子结点的路径字符串
            :param left: 左括号还可以使用的个数
            :param right: 右括号还可以使用的个数
            :return:
            """
            if left == 0 and right == 0:
                res.append(cur_str)
                return
            if right < left:
                return
            if left > 0:
                dfs(cur_str + '(', left - 1, right)
            if right > 0:
                dfs(cur_str + ')', left, right - 1)

        dfs(cur_str, n, n)
        return res


if __name__ == '__main__':
    s = Solution
    n = 3
