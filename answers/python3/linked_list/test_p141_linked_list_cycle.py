# coding: utf-8

__author__ = '代码会说话'


from list_node import  *

class Solution(object):
  def hasCycle(self, head:ListNode)->bool:
    if head is None:
      return False
    t = head # turtle
    r = head.next # rabbit
    while t and r and r.next:
      if t == r:
        return True
      t = t.next
      r = r.next.next
    return False


from list_node import  *
def test():
  s = Solution()
  l1 = arrayToList([3,2,0,-4])
  l1_pos1 = moveForward(l1, 1)
  l1_end = moveToEnd(l1)
  l1_end.next = l1_pos1

  assert s.hasCycle(l1)

  l2 = arrayToList([1,2])
  l2_end = moveToEnd(l2)
  l2_end.next = l2
  assert s.hasCycle(l2)