# -*- coding: utf-8 -*-
"""
   @FileName :   20.valid-parentheses.py
   @Email :      expbuf@hotmail.com
   @Date :       2021/03/09 19:50
   @Author :     expbuf
   @Description :
"""
__author__ = 'expbuf'
"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
示例 1：
    输入：s = "()"
    输出：true
示例 2：
    输入：s = "()[]{}"
    输出：true
示例 3：
    输入：s = "(]"
    输出：false
示例 4：
    输入：s = "([)]"
    输出：false
示例 5：
    输入：s = "{[]}"
    输出：true

提示：
    1 <= s.length <= 104
    s 仅由括号 '()[]{}' 组成
"""


class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'{': '}', '[': ']', '(': ')', '?': '?'}
        stack = ['?']
        for c in s:
            if c in dic:
                stack.append(c)
                print(stack)
            elif dic[stack.pop()] != c:
                print(stack)
                return False
        print(stack)
        print(len(stack))
        return len(stack) == 1


if __name__ == '__main__':
    s = Solution()
    symbol = "({}{})"
    r = s.isValid(symbol)
    print(r)
