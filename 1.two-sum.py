#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :    1.two-sum.py
@Contact :    expbuf@hotmail.com
@Datetime:    2021/3/1 16:46
@Author :     expbuf
'''

from typing import List


# 暴力破解
class Solution:
    def twoSum(self, nums, target):
        lens = len(nums)
        j = -1
        for i in range(lens):
            if (target - nums[i]) in nums:X-buf
                if (nums.count(target - nums[i]) == 1) & (
                        target - nums[i] == nums[i]):  # 如果num2=num1,且nums中只出现了一次，说明找到是num1本身。
                    continue
                else:
                    j = nums.index(target - nums[i], i + 1)  # index(x,i+1)是从num1后的序列后找num2
                    break
        if j > 0:
            return [i, j]
        else:
            return []


# 暴力搜索
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


# 排序+双指针
class Solution4:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = nums.copy()
        temp.sort()
        i = 0
        j = len(nums) - 1
        while i < j:
            if (temp[i] + temp[j]) > target:
                j = j - 1
            elif (temp[i] + temp[j]) < target:
                i = i + 1
            else:
                break
        p = nums.index(temp[i])
        nums.pop(p)
        k = nums.index(temp[j])
        if k >= p:
            k = k + 1
        return [p, k]


# 暴力优化
class Solution2:
    def twoSum(self, nums, target):
        lens = len(nums)
        j = -1
        for i in range(1, lens):
            temp = nums[:i]
            if (target - nums[i]) in temp:
                j = temp.index(target - nums[i])
                break
        if j >= 0:
            return [j, i]


# 字典模拟哈希
# 通过字典的方法，查找效率快很多，执行速度大幅缩短，共 88ms。
class Solution3:
    def twoSum(self, nums, target):
        lens = len(nums)
        j = -1
        for i in range(1, lens):
            temp = nums[:i]
            if (target - nums[i]) in temp:
                j = temp.index(target - nums[i])
                break
        if j >= 0:
            return [j, i]


if __name__ == '__main__':
    # s = Solution()
    s = Solution1()
    sum = [1, 2, 3]
    target = 3
    res = s.twoSum(sum, target)
    # s.twoSum(sum, target)
    print(res)
