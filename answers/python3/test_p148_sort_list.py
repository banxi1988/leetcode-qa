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

  def sortList_insert(self, head:ListNode) -> ListNode:
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

  def merge(self,l1:ListNode, l2:ListNode):
    if l1 is None:
      return l2
    if l2 is None:
      return  l1
    p1 = l1
    p2 = l2
    start = ListNode(0)
    p = start
    while p1 and p2:
      if p1.val < p2.val:
        p.next = p1
        p1 = p1.next
      else:
        p.next = p2
        p2 = p2.next
      p = p.next
    p.next = p2 if p2 else p1
    return start.next

  def move_forward(self,head:ListNode, max_steps:int):
    """ 向前走 max_steps 后返回指向的节点，返回节点不为空 """
    # 2,3
    p = head
    i = 0
    while i < max_steps and p.next:
      i += 1
      p = p.next
    return p

  def move_to_end(self,head:ListNode):
    """ 移动到链表尾部 """
    p = head
    while p.next:
      p = p.next
    return p



  def sortList_merge(self, head:ListNode) -> ListNode:
    if head is None or head.next is None:
      return head
    start = ListNode(0)
    start.next = head
    merge_size = 1
    while True:
      p = start.next
      prev_p = start
      merge_count = 0
      while p:
        # 划分链表
        l1_start = p
        l1_end = self.move_forward(l1_start, merge_size -1)
        l2_start = l1_end.next
        l1_end.next = None
        if l2_start:
          l2_end = self.move_forward(l2_start, merge_size -1)
          next_p = l2_end.next
          l2_end.next = None
        else:
          next_p = None
        l3_start = self.merge(l1_start,l2_start)
        prev_p.next = l3_start
        prev_p = self.move_to_end(prev_p)
        p = next_p
        merge_count += 1
      if merge_count == 1:
        break
      merge_size *= 2

    return start.next


  sortList = sortList_merge

def test():
  s = Solution()
  l3 = arrayToList([8,3,2,1,6,4,7,5])
  assert [1,2,3,4,5,6,7,8] == listToArray(s.sortList(l3))
  l1 = arrayToList([4,2,1,3])
  assert [1,2,3,4] == listToArray(s.sortList(l1))

  l2 = arrayToList([-1,5,3,4,0])
  assert [-1,0,3,4,5] == listToArray(s.sortList(l2))

  l4 = arrayToList([3,2,1])
  assert [1,2,3] == listToArray(s.sortList(l4))

  l5 = arrayToList([3,2])
  assert [2,3] == listToArray(s.sortList(l5))

  l6 = arrayToList([3])
  assert [3] == listToArray(s.sortList(l6))

