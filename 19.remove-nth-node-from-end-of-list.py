# -*- coding: utf-8 -*-
"""
   @FileName :   19.remove-nth-node-from-end-of-list.py
   @Email :      expbuf@hotmail.com
   @Date :       2021/03/09 15:32
   @Author :     expbuf
   @Description :
"""
__author__ = 'expbuf'

import pdb
from typing import List

"""
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
进阶：你能尝试使用一趟扫描实现吗？
示例 1：
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
示例 2：
输入：head = [1], n = 1
输出：[]
示例 3：
输入：head = [1,2], n = 1
输出：[1]

提示：
    链表中结点的数目为 sz
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz
    
解法：
    两边遍历法
    递归法
    快慢指针法
    
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # pdb.set_trace()

        def getLength(head: ListNode) -> int:
            length = 0
            while head:
                length += 1
                head = head.next
            return length

        dummy = ListNode(0, head)
        length = getLength(head)
        cur = dummy
        for i in range(1, length - n + 1):
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next


# 栈
class Solution1:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        stack = list()
        cur = dummy
        while cur:
            stack.append(cur)
            cur = cur.next

        for i in range(n):
            stack.pop()

        prev = stack[-1]
        prev.next = prev.next.next
        return dummy.next


if __name__ == '__main__':
    s = Solution1()
    head = [1, 2, 3, 4, 5]
    head = ListNode(head)
    # print(head)
    # LN(head)
    n = 3
    res = s.removeNthFromEnd(head, n)
    print(res)
