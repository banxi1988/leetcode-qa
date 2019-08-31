# coding: utf-8

__author__ = '代码会说话'

"""
[LeetCode 1171]. 从链表中删去总和值为零的连续节点(难度:中等)

给你一个链表的头节点 head，请你编写代码，
反复删去链表中由 总和 值为 0 的连续节点组成的序列，直到不存在这样的序列为止。

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

 1,2,3,-3,-2 
 
1) 求任意子链表,子组数和的 O(N) 算法
 arr[i]+arr[i+1]+..+ arr[j] 
 
 sumi = arr[0] +.. + arr[i]
 sumj = arr[0] +.. + arr[j]
 sumij = sumj - sumi
 
 node.sum = 0
 
 node0.sum = node0.val
 node1.sum = node1.val + node0.sum
 nodeN.sum = nodeN.val + node(n-1).sum

2)
  node0..node3 

dummy -> node0
dummy - > node4

return dummy->next

  node2.sum - dummy.sum == 0

  [0..k]
  [1..k]

提示：

给你的链表中可能有 1 到 1000 个节点。
对于链表中的每个节点，节点的值：-1000 <= node.val <= 1000.
"""
from list_node import ListNode, arrayToList,listToArray


class Solution:

  def removeZeroSumSublists(self, head: ListNode) -> ListNode:
    dummy = ListNode(0)
    dummy.sum = 0
    dummy.next = head
    cur_sum = 0
    p = head
    while p:
      cur_sum += p.val
      p.sum = cur_sum
      p = p.next

    start = dummy
    while start:
      cur  = start.next # node0
      while cur:
        range_sum = cur.sum - start.sum
        if range_sum == 0:
           start.next = cur.next  # delete start->next 到 cur
           break
        else:
          cur = cur.next
      start = start.next
    return dummy.next






def test():
  s = Solution()
  l5 = arrayToList([0,3,-1])
  l5_res = listToArray(s.removeZeroSumSublists(l5))
  assert l5_res == [3,-1]

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


