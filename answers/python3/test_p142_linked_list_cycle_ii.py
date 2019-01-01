# coding: utf-8

__author__ = '代码会说话'

"""
数据结构链表(6) 龟兔赛跑与环形链表检测  by 代码会说话

给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

说明：不允许修改给定的链表。 Floyd
              .
    : 1,2,3,4,5,6,7
            |_____|
            
slow: 1 2 3 4 5 
fast: 1 3 5 7 5

a: 1->4
b: 4->5
c: 5->4

slow: s   = a + b
fast: 2s  = a + b + c + b
a + b = c + b
a = c
        
"""

from list_node import  *

class Solution(object):
  def detectCycle(self, head:ListNode):
    if head is None or head.next is None:
      return  None

    slow = head
    fast = head
    has_cycle = False
    while slow and fast and fast.next:
      slow = slow.next
      fast = fast.next.next
      if slow and slow == fast:
        has_cycle = True
        break
    if not has_cycle:
      return  None
    p1 = head
    p2 = slow

    while p1 != p2:
      p1 = p1.next
      p2 = p2.next
    return  p1








def test():
  s = Solution()
  l1 = arrayToList([3,2,0,-4])
  l1_pos1 = moveForward(l1, 1)
  l1_end = moveToEnd(l1)
  l1_end.next = l1_pos1

  assert s.detectCycle(l1) == l1_pos1

  l2 = arrayToList([1,2])
  l2_end = moveToEnd(l2)
  l2_end.next = l2
  assert s.detectCycle(l2) == l2

  l3 = arrayToList([1,2,3,4,5,6])
  l3_end = moveToEnd(l3)
  l3_end.next = l3.next
  assert s.detectCycle(l3) == l3.next
