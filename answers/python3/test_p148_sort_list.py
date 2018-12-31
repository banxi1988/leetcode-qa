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

4->2->1->3
2->4->1->3
1->2->3->4

-1->5->3->4->0
-1->5->3->4->0
-1->4->3->5->0

i,i+1,i+2,i+3

1) 第一次比较
2i vs 2i+1
0 vs 1
2 vs 3

0,2,4,6
1,3,5,7

7,6,5,4,3,2
6,7,4,5,2,3
4,5

4,5,6,7
2i < 2i+1

3i < 3i + 1
i < i + 1


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
    p.next = p2 if p2 else p1
    return start.next



  def sortList_merge(self, head:ListNode) -> ListNode:
    if head is None or head.next is None:
      return head
    start = ListNode(0)
    start.next = head
    # s 8,  3,  2, 1,6,4,7,5
    # p p1, p2, p
    merge_size = 1
    while True:
      p = start.next
      prev_p = start
      merge_count = 0
      while p:
        i = 0
        # 划分链表
        p1 = p
        p2 = p1
        p1_end = p2
        while i < merge_size and p2:
          p1_end = p2
          i+= 1
          p2 = p2.next
        i = 0
        p1_end.next = None
        p2_end = p2
        next_p = p2
        while i< merge_size and next_p:
          i+= 1
          p2_end = next_p
          next_p = next_p.next
        if p2_end:
          p2_end.next = None

        # 合并
        p = prev_p
        while p1 and p2:
          if p1.val < p2.val:
            p.next = p1
            p1 = p1.next
          else:
            i+= 1
            p.next = p2
            p2 = p2.next
          p = p.next

        p.next =  p2 if p2 else p1
        prev_p = p
        while prev_p.next:
          prev_p = prev_p.next
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
