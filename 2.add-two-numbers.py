# Definition for singly-linked list.
import pdb


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None

    def initList(self, data):
        # 创建头结点
        self.head = ListNode(data[0])
        r = self.head
        p = self.head
        # 逐个为 data 内的数据创建结点, 建立链表
        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next
        return r

    def printlist(self, head):
        if head == None: return
        node = head
        while node != None:
            print(node.val, end='')
            node = node.next

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = p = ListNode(None)  # 保存头结点，返回结果
        s = 0  # 每一步的求和暂存变量
        # pdb.set_trace()
        while l1 or l2 or s:  # 循环条件：l1 或者l2（没有遍历完成），s(进位)不为0
            s += (l1.val if l1 else 0) + (l2.val if l2 else 0)  # 这其实是好多代码，我自己写了好多行，但是作者这样写非常简洁，赞
            p.next = ListNode(s % 10)  # 构建新的list存储结果，其实用较长的加数链表存也可以，%10：求个位
            p = p.next
            s //= 10  # 求进位
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
        # print(dummy.next)


# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         dummy = p = ListNode(None)  # 保存头结点，返回结果
#         s = 0  # 每一步的求和暂存变量
#         while l1 or l2 or s:  # 循环条件：l1 或者l2（没有遍历完成），s(进位)不为0
#             s += (l1.val if l1 else 0) + (l2.val if l2 else 0)  # 这其实是好多代码，我自己写了好多行，但是作者这样写非常简洁，赞
#             p.next = ListNode(s % 10)  # 构建新的list存储结果，其实用较长的加数链表存也可以，%10：求个位
#             p = p.next
#             s //= 10  # 求进位
#             l1 = l1.next if l1 else None
#             l2 = l2.next if l2 else None
#         return dummy.next
#         print(dummy.next)


if __name__ == '__main__':
    l = LinkList()
    data1 = [1, 2, 3]
    data2 = [2, 4, 6]
    l1 = l.initList(data1)
    l2 = l.initList(data2)
    l.printlist(l1)
    print('\n')
    l.printlist(l2)
    print('\n')

    # L = ListNode
    # # l1 = [1, 3, 9]
    # l1 = 1
    # # l2 = [0, 6, 8]
    # l2 = 0
    # # l1 = ListNode(l1)
    # # l2 = ListNode(l2)

    # S = Solution()

    # l1 = L(l1)
    # l2 = L(l2)
    # print(l1)
    # print(l2)
    # l.addTwoNumbers(l1, l2)
    # print(l.addTwoNumbers(l1, l2))
    a = l.addTwoNumbers(l1, l2)
    print(l.printlist(l.addTwoNumbers(l1, l2)))
    print(l.printlist(a))
    # [0,1,2,3,4,5,6,7,8,9]

    print(l1.val)
    print(l2.val)
    print(a.val)
    print(a.val)
