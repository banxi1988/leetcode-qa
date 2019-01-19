# coding: utf-8

__author__ = '代码会说话'
"""
设计一个找到数据流中第K大元素的类（class）。注意是排序后的第K大元素，不是第K个不同的元素。

你的 KthLargest 类需要一个同时接收整数 k 和整数数组nums 的构造器，它包含数据流中的初始元素。每次调用 KthLargest.add，返回当前数据流中第K大的元素。

示例:

int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8
说明: 
你可以假设 nums 的长度≥ k-1 且k ≥ 1。
"""

from typing import List
from tree_node import *

# class TreeNode:
#   def __init__(self,val:int):
#     self.val = val
#     self.count = 1
#     self.left = None # type: TreeNode
#     self.right = None # type: TreeNode

class BST:
  def __init__(self):
    self.root = None # type: TreeNode

  def insert(self,val:int):
    if self.root:
      self._insert(self.root, val)
    else:
      self.root = TreeNode(val)
      self.root.count = 1


  def _insert(self,branch:TreeNode,val:int):
    parent = branch
    while parent:
      parent.count += 1
      if parent.val > val:
        if parent.left:
          parent = parent.left
        else:
          left = TreeNode(val)
          left.count = 1
          parent.left = left
          break
      else:
        if parent.right:
          parent = parent.right
        else:
          right = TreeNode(val)
          right.count = 1
          parent.right = right
          break

  def find_kth_num(self,k:int):
    def find_right_most(branch:TreeNode) -> int:
      right = branch
      while right.right:
        right = right.right
      return right.val
    def find_left_most(branch:TreeNode) -> int:
      left = branch
      while left.left:
        left = left.left
      return left.val
    def find_kth_num_in(branch:TreeNode,k:int):
      assert branch is not None

      while branch:
        if branch.count == k:
          return find_left_most(branch)
        else:
          if k == 1:
            return find_right_most(branch)
        left = branch.left
        right = branch.right
        if right:
          right_count = right.count
          if right_count + 1 == k:
            return branch.val
          elif right_count + 1 < k:
            branch = left
            k -= right_count + 1
          else:
            branch = right
        else:
          branch = left
          k -= 1

    return find_kth_num_in(self.root, k)


class KthLargest:

  def __init__(self, k:int, nums:List[int]):
    self.k = k
    self.bst = BST()
    if nums:
      for num in nums:
        self.bst.insert(num)

  def add(self, val:int) -> int:
    self.bst.insert(val)
    return self.bst.find_kth_num(self.k)


def test():
  kth = KthLargest(3, [4,5,8,2])
  assert kth.add(3) == 4
  assert kth.add(5) == 5
  assert kth.add(10) == 5
  assert kth.add(9) == 8
  assert kth.add(4) == 8

  kth2 = KthLargest(1,[])
  assert kth2.add(3) == 3
  assert kth2.add(2) == 3
  assert kth2.add(3) == 3
  assert kth2.add(4) == 4
  assert kth2.add(1) == 4
  assert kth2.add(0) == 4
  assert kth2.add(4) == 4
  assert kth2.add(5) == 5
