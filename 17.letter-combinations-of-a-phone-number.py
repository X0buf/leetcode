# -*- coding: utf-8 -*-
"""
   @FileName :   17.letter-combinations-of-a-phone-number.py
   @Email :      expbuf@hotmail.com
   @Date :       2021/03/08 11:31
   @Author :     expbuf
   @Description :
"""
__author__ = 'expbuf'

"""
17. 电话号码的字母组合
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例 1：
输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
示例 2：
输入：digits = ""
输出：[]
示例 3：
输入：digits = "2"
输出：["a","b","c"]
"""

from typing import List
import pdb


# 回溯
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # print(digits)
        if not digits:
            return list()
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index: int):
            pdb.set_trace()

            if index == len(digits):
                combinations.append("".join(combination))
            else:
                digit = digits[index]
                print("=====")
                print(digit)
                for letter in phoneMap[digit]:
                    print(letter)
                    print(phoneMap[digit])
                    combination.append(letter)
                    print(combination)
                    backtrack(index + 1)
                    combination.pop()

        combination = list()
        combinations = list()
        backtrack(0)

        return combinations


if __name__ == '__main__':
    # a = [1, 1, 1]
    # a.pop()
    # b = list()
    # print(type(a))
    # print(type(b))
    s = Solution()
    # s = Solution1()
    digits = "23"
    # target = 3
    res = s.letterCombinations(digits)
    # s.twoSum(sum, target)
    print(res)
