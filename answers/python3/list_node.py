# coding: utf-8

__author__ = '代码会说话'

from typing import List,Optional
# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None # type: ListNode

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


def reverseList2(head:Optional[ListNode]):
  if head is None or head.next is None:
    return head
  prev = ListNode(0)
  p = head
  # 1,2,3
  # prev -> 1
  # prev -> 2 -> 1
  while p is not  None:
    old_next = prev.next # 1
    prev.next = p # prev->2
    p = p.next #
    prev.next.next = old_next
  return prev.next


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
