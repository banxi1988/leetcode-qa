# coding: utf-8

__author__ = '代码会说话'


from list_node import  *

class Solution(object):
  def detectCycle(self, head:ListNode):
    if head is None or head.next is None:
      return None
    slow = head
    fast = head
    hasCycle = False
    while slow and fast and fast.next:
      slow = slow.next
      fast = fast.next.next
      if slow and slow == fast:
        hasCycle = True
        break
    if not hasCycle:
      return None
    q = head
    while q != slow:
      q = q.next
      slow = slow.next
    return q



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
