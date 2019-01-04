# coding: utf-8

__author__ = '代码会说话'

"""
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6
"""

from list_node import *

from typing import List

class Solution:
  def mergeKLists(self, lists:List[ListNode])->ListNode:
    if not lists:
      return None
    if len(lists) < 2:
      return  lists[0]
    heads = [head for head in lists]
    while len(heads) > 1:
      next_heads = []
      head_count = len(heads)
      for i in range(0,head_count-1, 2):
        l1 = heads[i]
        l2 = heads[i+1]
        merged = mergeTwoSortedLists(l1,l2)
        next_heads.append(merged)
      if head_count % 2 == 1:
        next_heads.append(heads[-1])
      heads = next_heads
    return heads[0]





def test():
  s = Solution()
  l1 = arrayToList([1,4,5])
  l2 = arrayToList([1,3,4])
  l3 = arrayToList([2,6])

  r1 = s.mergeKLists([l1,l2,l3])
  assert [1,1,2,3,4,4,5,6] == listToArray(r1)

