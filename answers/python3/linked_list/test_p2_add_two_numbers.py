# coding: utf-8

__author__ = '代码会说话'

"""
数据结构链表(4)两个链表表示的数相加 by 代码会说话

给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) 
     (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

16 位
3->4->2
4->6->5

2->4->3
5->6->4

6->9
6

96 + 6 = 102
2->0->1
"""

from list_node import *

class Solution:
  def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if l1 is None:
      return  l2
    if l2 is None:
      return  l1

    p1 = l1
    p2 = l2
    carry = 0 # 进位
    start = ListNode(0)
    p = start
    while p1 or p2:
      val1 = p1.val if p1 else 0
      val2 = p2.val if p2 else 0
      sum = val1 + val2 + carry

      val = sum % 10
      carry = sum // 10
      p.next = ListNode(val)
      p = p.next

      p1 = p1.next if p1 else None
      p2 = p2.next if p2 else None
    if carry > 0:
      p.next = ListNode(carry)

    return start.next






def test():
  s = Solution()

  l4 = arrayToList([6,9])
  l5 = arrayToList([6])
  l6 = s.addTwoNumbers(l4,l5)
  # 96 + 6 = 102
  expected2 = [2,0,1]
  actual2 = listToArray(l6)
  assert  actual2 == expected2

  l1 = arrayToList([2,4,3])
  l2 = arrayToList([5,6,4])
  expected1 = [7,0,8]
  l3 = s.addTwoNumbers(l1,l2)
  actual1 = listToArray(l3)
  assert expected1 == actual1


