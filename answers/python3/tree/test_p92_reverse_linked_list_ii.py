# coding: utf-8

__author__ = '代码会说话'

"""
数据结构链表(2)反转链表I,II by 代码会说话
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL

l1 :1
l2: 2->3->4
l3: 5

"""
from list_node import  *

class Solution:

  def reverseBetween(self, head, m:int, n:int):
    """
    :type head: ListNode
    :rtype: ListNode
    l1 :1
    l2: 2->3->4
    l3: 5
    """
    if m == n:
      return head
    l1end = None
    p = head
    for _ in range(1,m):
      l1end = p
      p = p.next
    l2start = p
    l2end = None
    for _ in range(m,n + 1):
      l2end = p
      p = p.next

    l3start = p
    l2end.next = None

    reversed_l2 = self.reverseList(l2start)
    l2start.next = l3start
    if l1end:
      l1end.next = reversed_l2
      return head
    else:
      return reversed_l2









def test():
  s = Solution()
  assert [3,2,1] == listToArray(s.reverseList(arrayToList([1,2,3])))
  l1 = arrayToList([1,2,3,4,5])
  r1 = s.reverseBetween(l1, 2,4)
  assert [1,4,3,2,5] == listToArray(r1)

  l2 = arrayToList([1,2,3,4,5])
  r2 = s.reverseBetween(l2, 1,4)
  assert [4,3,2,1,5] == listToArray(r2)

