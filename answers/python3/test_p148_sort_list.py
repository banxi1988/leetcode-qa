# coding: utf-8

__author__ = '代码会说话'

"""
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:

输入: 4->2->1->3
输出: 1->2->3->4
示例 2:

输入: -1->5->3->4->0
输出: -1->0->3->4->5
"""
from list_node import  *

class SortedLinkedList:
  def __init__(self,head):
    self.head = head #type: ListNode

  def _insertHead(self,node):
    old_head = self.head
    self.head = node
    node.next = old_head

  def insert(self,node):
    p = self.head
    if self.head.val > node.val:
      return self._insertHead(node)
    prev = p
    # 1,2,3
    while p and p.val < node.val:
      prev = p
      p = p.next
    old_next = prev.next
    node.next = old_next
    prev.next = node






class Solution:


  def sortList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head is None or head.next is None:
      return head
    p = head.next
    sll = SortedLinkedList(head)
    head.next = None
    while p :
      tmp = p
      p = p.next
      tmp.next = None
      sll.insert(tmp)

    return sll.head


def test():
  s = Solution()
  l1 = arrayToList([4,2,1,3])
  assert [1,2,3,4] == listToArray(s.sortList(l1))

  l2 = arrayToList([-1,5,3,4,0])
  assert [-1,0,3,4,5] == listToArray(s.sortList(l2))
