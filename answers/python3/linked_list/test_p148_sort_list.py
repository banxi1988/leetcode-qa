# coding: utf-8

__author__ = '代码会说话'

"""
数据结构链表(5) 链表的最佳排序方法-向上的归并排序 by 代码会说话

在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:

输入: 4->2->1->3
输出: 1->2->3->4
示例 2:

输入: -1->5->3->4->0
输出: -1->0->3->4->5

   8,3,2,1,6,4,7,5
1: 3,8,1,2,4,6,5,7  1
2: 1,2,3,8,4,5,6,7  2
3: 1,2,3,4,5,6,7,8  4




"""
from list_node import  *



class Solution:

  def move_to_end(self,head:ListNode):
    p = head
    while p.next:
      p = p.next
    return p

  def move(self,head:ListNode, steps:int):
    p = head
    i = 0
    while i < steps and p.next:
      i += 1
      p = p.next
    return p



  def sortList(self, head:ListNode) -> ListNode:
    if head is None or head.next is None:
      return head
    """
   8,3,2,1,6,4,7,5
1: 3,8,1,2,4,6,5,7  1
2: 1,2,3,8,4,5,6,7  2
3: 1,2,3,4,5,6,7,8  4
    """
    list_size = 1
    start = ListNode(0)
    start.next = head
    while True:
      merge_count = 0
      p = start.next
      prev_p = start
      while p:
        l1_start = p
        l1_end = self.move(l1_start, list_size -1)
        l2_start = l1_end.next
        l1_end.next = None
        if l2_start:
          l2_end = self.move(l2_start, list_size -1)
          next_p = l2_end.next
          l2_end.next = None
        else:
          l2_end = None
          next_p = None

        merged_list = mergeTwoSortedLists(l1_start, l2_start)

        prev_p.next = merged_list

        p = next_p
        prev_p = self.move_to_end(prev_p)
        merge_count += 1

      if merge_count == 1:
        break
      list_size *=2
    return start.next

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

