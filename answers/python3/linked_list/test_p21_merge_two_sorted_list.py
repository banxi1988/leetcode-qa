# coding: utf-8

__author__ = '代码会说话'

"""
数据结构链表(1)合并有序链表 by 代码会说话
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""
from list_node import  *


class Solution:
  def mergeTwoLists(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if l1 is None:
      return  l2
    if l2 is None:
      return l1
    p1 = l1
    p2 = l2
    start = ListNode(0)
    p = start
    while p1 and p2:
      if p1.val < p2.val:
        p.next  = p1
        p1 = p1.next
      else:
        p.next = p2
        p2 = p2.next
      p = p.next
    p.next = p1 if p1 else p2

    return start.next



def test():
  l1 = arrayToList([1,2,4])
  l2 = arrayToList([1,3,4])

  s = Solution()
  m1 = s.mergeTwoLists(l1,l2)
  assert [1,1,2,3,4,4] == listToArray(m1)
