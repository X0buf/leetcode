# -*- coding: utf-8 -*-
"""
   @FileName :   23.merge-k-sorted-lists.py
   @Email :      expbuf@hotmail.com
   @Date :       2021/03/11 11:14
   @Author :     expbuf
   @Description :
"""
__author__ = 'expbuf'

"""
23.合并K个升序链表
    给你一个链表数组，每个链表都已经按升序排列。
    请你将所有链表合并到一个升序链表中，返回合并后的链表。

示例 1：
    输入：lists = [[1,4,5],[1,3,4],[2,6]]
    输出：[1,1,2,3,4,4,5,6]
    解释：链表数组如下：
    [
      1->4->5,
      1->3->4,
      2->6
    ]
    将它们合并到一个有序链表中得到。
    1->1->2->3->4->4->5->6
示例 2：
    输入：lists = []
    输出：[]
示例 3：
    输入：lists = [[]]
    输出：[]

提示：
    k == lists.length
    0 <= k <= 10^4
    0 <= lists[i].length <= 500
    -10^4 <= lists[i][j] <= 10^4
    lists[i] 按 升序 排列
    lists[i].length 的总和不超过 10^4

解法：
    暴力
    优先队列
    分治法
"""

from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 暴力
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists or len(lists) == 0:
            return None
        import heapq
        all_vals = []
        for l in lists:
            while l:
                all_vals.append(l.val)
                l = l.next
        all_vals.sort()
        dummy = ListNode(None)
        cur = dummy
        for i in all_vals:
            temp_node = ListNode(i)
            cur.next = temp_node
            cur = temp_node

        return dummy.next


# 优先队列
class Solution1:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists or len(lists) == 0:
            return None
        import heapq
        heap = []
        # 首先 for 嵌套 while 就是将所有元素都取出放入堆中
        for node in lists:
            while node:
                heapq.heappush(heap, node.val)
                node = node.next
        dummy = ListNode(None)
        cur = dummy
        # 依次将堆中的元素取出(因为是小顶堆，所以每次出来的都是目前堆中值最小的元素），然后重新构建一个列表返回
        while heap:
            temp_node = ListNode(heappop(heap))
            cur.next = temp_node
            cur = temp_node
        return dummy.next


# 分治
class Solution2:
    def merge(self, node_a, node_b):
        dummy = ListNode(None)
        cursor_a, cursor_b, cursor_res = node_a, node_b, dummy
        while cursor_a and cursor_b:  # 对两个节点的 val 进行判断，直到一方的 next 为空
            if cursor_a.val <= cursor_b.val:
                cursor_res.next = ListNode(cursor_a.val)
                cursor_a = cursor_a.next
            else:
                cursor_res.next = ListNode(cursor_b.val)
                cursor_b = cursor_b.next
            cursor_res = cursor_res.next
        # 有一方的next的为空，就没有比较的必要了，直接把不空的一边加入到结果的 next 上
        if cursor_a:
            cursor_res.next = cursor_a
        if cursor_b:
            cursor_res.next = cursor_b
        return dummy.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        length = len(lists)

        # 边界情况
        if length == 0:
            return None
        if length == 1:
            return lists[0]

        # 分治
        mid = length // 2
        return self.merge(self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:length]))


if __name__ == '__main__':
    s = Solution()
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    ListNode = ListNode()
    lists = ListNode(lists)
    r = s.mergeKLists(lists)
    print(r)
