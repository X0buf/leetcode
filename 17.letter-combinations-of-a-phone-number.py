# -*- coding: utf-8 -*-
"""
   @FileName :   17.letter-combinations-of-a-phone-number.py
   @Email :      expbuf@hotmail.com
   @Date :       2021/03/08 11:31
   @Author :     expbuf
   @Description :
"""
__author__ = 'expbuf'

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
