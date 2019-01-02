# coding: utf-8

__author__ = '代码会说话'

"""
数据结构链表(7) 寻找相交链表的起始点 by 代码会说话

编写一个程序，找到两个单链表相交的起始节点。

如下面的两个链表：



在节点 c1 开始相交。

示例 1：

5->0->2
       \
  4->1->8->4->5

pA: 5 0 2 8 4 5   4 1 8
pB: 4 1 8 4 5  5 0 2 8

5->0->2->8->4->5

   4->1->8->4->5


输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,2,8,4,5], skipA = 2, skipB = 3
输出：Reference of the node with value = 8
输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,2,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
 

示例 2：



输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Reference of the node with value = 2
输入解释：相交节点的值为 2 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。
 

示例 3：



输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
输出：null
输入解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
解释：这两个链表不相交，因此返回 null。
 

注意：

如果两个链表没有交点，返回 null.
在返回结果后，两个链表仍须保持原有的结构。
可假定整个链表结构中没有循环。
程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。

"""

from list_node import *
from typing import Optional

class Solution(object):
  def getIntersectionNode(self, headA:ListNode, headB:ListNode) -> Optional[ListNode]:
    if headA is None or headB is None:
      return None
    endA = moveToEnd(headA)
    endB = moveToEnd(headB)
    if endA != endB:
      return None
    pA = headA
    pB = headB
    while pA != pB:
      pA = pA.next if pA.next else headB
      pB = pB.next if pB.next else headA
    return pA




def test():
  l1 = arrayToList([8,4,5])

  l2 = arrayToList([4,1])
  l3 = arrayToList([5,0,2])
  l2_end = moveToEnd(l2)
  l3_end = moveToEnd(l3)
  l2_end.next = l1
  l3_end.next = l1

  s = Solution()
  assert s.getIntersectionNode(l2,l3) == l1

  l4 = arrayToList([2,6,4])
  l5 = arrayToList([1,5])
  assert s.getIntersectionNode(l4,l5) == None
