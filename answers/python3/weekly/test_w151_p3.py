# coding: utf-8

__author__ = '代码会说话'

"""
给你一个链表的头节点 head，请你编写代码，反复删去链表中由 总和 值为 0 的连续节点组成的序列，直到不存在这样的序列为止。

删除完毕后，请你返回最终结果链表的头节点。

 

你可以返回任何满足题目要求的答案。

（注意，下面示例中的所有序列，都是对 ListNode 对象序列化的表示。）

示例 1：

输入：head = [1,2,-3,3,1]
输出：[3,1]
提示：答案 [1,2,1] 也是正确的。
示例 2：

输入：head = [1,2,3,-3,4]
输出：[1,2,4]
示例 3：

输入：head = [1,2,3,-3,-2]
输出：[1]
 

提示：

给你的链表中可能有 1 到 1000 个节点。
对于链表中的每个节点，节点的值：-1000 <= node.val <= 1000.
"""
from list_node import ListNode

from typing import List,Optional
from functools import lru_cache
from collections import defaultdict, Counter

def arrayToList(nums:List[int]) -> Optional[ListNode]:
  if not nums:
    return None
  head = ListNode(nums[0])
  p = head
  for num in nums[1:]:
    p.next = ListNode(num)
    p = p.next
  return  head

def listToArray(head:Optional[ListNode]) -> List[int]:
  if not head:
    return []
  p = head
  nums = []
  while p is not None:
    nums.append(p.val)
    p = p.next
  return nums

class Solution:
  def removeZeroSumSubArr(self, arr: List[int]) -> List[int]:
    N = len(arr)
    if N == 1:
      if arr[0] == 0:
        return []
      else:
        return arr
    SN = N + 1
    sums = [0] * SN
    cur_sum = 0
    for i,num in enumerate(arr):
      cur_sum += num
      sums[i+1] = cur_sum

    if sums[-1] == 0:
      return []
    i = None
    j = None
    found = False
    for i in range(N):
      found = False
      for j in range(N,i,-1):
        sumij = sums[j] - sums[i]
        if sumij == 0:
          found = True
          break
      if found:
        break
    if found:
      del arr[i:j]
      return self.removeZeroSumSubArr(arr)
    else:
      return arr


  def removeZeroSumSublists(self, head: ListNode) -> ListNode:
    arr = listToArray(head)
    res = self.removeZeroSumSubArr(arr)
    return arrayToList(res)


def test():
  s = Solution()

  l1 = arrayToList([1,2,-3,3,1])
  l1_res = listToArray( s.removeZeroSumSublists(l1) )

  assert l1_res in [
    [3,1],
    [1,2,1]
  ]

  l2 = arrayToList([1,2,3,-3,4])
  l2_res = listToArray(s.removeZeroSumSublists(l2))
  assert l2_res == [1,2,4]

  l3 = arrayToList([1,2,3,-3,-2])
  l3_res =  listToArray(s.removeZeroSumSublists(l3))
  assert l3_res == [1]

  l4 = arrayToList([-1,1])
  l4_res = listToArray(s.removeZeroSumSublists(l4))

  assert l4_res == []

