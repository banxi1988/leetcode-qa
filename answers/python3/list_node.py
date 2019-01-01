# coding: utf-8

__author__ = '代码会说话'

from typing import List,Optional
# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None # type: ListNode

  def __str__(self):
    values = [self.val]
    if hasCycle(self):
      return str(self.val) + "->0"
    p = self.next
    while p:
      values.append(p.val)
      p = p.next
    return "->".join(map(str,values))

def hasCycle(head:ListNode):
  """ 检测单链表是否有环"""
  slow = head
  fast = head
  while slow and fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow and slow == fast:
      return  True
  return False

def detectCycle(head:ListNode):
  """返回链表有环的起始节点"""
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

def reverseList(head:Optional[ListNode]):
  if head is None or head.next is None:
    return head
  #1,2,3
  #3,2,1
  stack = []
  p = head
  while p is not None:
    stack.append(p)
    p = p.next

  start = ListNode(0)
  p = start
  while stack:
    p.next = stack.pop()
    p = p.next
  p.next = None # NOTE,不置空容易造成循环链表
  return start.next

def reverseListR(head:Optional[ListNode]):
  if head is None or head.next is None:
    return head
  #1
  # 2,3
  # 3,2
  reverse_start = head.next
  reversed_end = reverse_start
  reversed_start = reverseListR(reverse_start)
  reversed_end.next = head
  head.next = None
  return reversed_start



def reverseList2(head:Optional[ListNode]):
  """ 数据结构链表(3)只用一个循环的反转链表方法解析 by 代码会说话"""
  # 1,2,3
  # start -> 1
  # start ->2 -> 1
  if head is None or head.next is None:
    return head

  start = ListNode(0)
  p = head
  while p is not None:
    old_start_next = start.next
    start.next = p
    p = p.next
    start.next.next = old_start_next

  return start.next

def mergeTwoSortedLists(l1:Optional[ListNode], l2: Optional[ListNode]) ->ListNode:
  """合并两个有序链表"""
  if l1 is None:
    return  l2
  if l2 is None:
    return l1
  p1 = l1
  p2 = l2
  start = ListNode(0)
  p = start
  while p1 and p2:
    if p1.val < p2.val:
      p.next  = p1
      p1 = p1.next
    else:
      p.next = p2
      p2 = p2.next
    p = p.next
  p.next = p1 if p1 else p2

  return start.next

def moveToEnd(head:ListNode) -> ListNode:
    p = head
    while p.next:
      p = p.next
    return p

def moveForward(head:ListNode, steps:int) -> ListNode:
  p = head
  i = 0
  while i < steps and p.next:
    i += 1
    p = p.next
  return p


def test_merge_two_sorted_list():
  l1 = arrayToList([1, 2, 4])
  l2 = arrayToList([1, 3, 4])

  m1 = mergeTwoSortedLists(l1, l2)
  assert [1, 1, 2, 3, 4, 4] == listToArray(m1)


def test_list_nodes():
  nums1 = [1,2,4]
  l1 = arrayToList(nums1)
  assert nums1 == listToArray(l1)
  nums2 = [1,3,4]
  l2 = arrayToList([1,3,4])
  assert nums2 == listToArray(l2)

def test_reverse_list():
  l1 = arrayToList([1,2,3])
  l2 = reverseList(l1)
  assert [3,2,1] == listToArray(l2)
  l1 = arrayToList([1,2,3])
  l3 = reverseList2((l1))
  assert [3,2,1] == listToArray(l3)
  l1 = arrayToList([1,2,3])
  l4 = reverseListR((l1))
  assert [3,2,1] == listToArray(l4)

