# coding: utf-8

__author__ = '代码会说话'
"""
数据结构二叉树(6）另一种层序遍历
 
103. 二叉树的锯齿形层次遍历


给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层次遍历如下：

[
  [3],
  [20,9],
  [15,7]
]

"""
from tree_node import *
from typing import List


class Solution:
  def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
    if not root:
      return []
    level_nodes = [root]
    left_to_right = True
    results = []
    while level_nodes:
      nums = [] if left_to_right else deque()
      next_level_nodes = []
      for node in level_nodes:
        if left_to_right:
          nums.append(node.val)
        else:
          nums.insert(0, node.val)  # O(n) vs O(1)
        left = node.left
        right = node.right
        if left:
          next_level_nodes.append(left)
        if right:
          next_level_nodes.append(right)

      if left_to_right:
        results.append(nums)
      else:
        results.append(list(nums))
      left_to_right = not left_to_right
      level_nodes = next_level_nodes

    return results


def test():
  s = Solution()
  t1 = make_simple_tree(3, 9, make_simple_tree(20, 15, 7))

  assert [
           [3],
           [20, 9],
           [15, 7]
         ] == s.zigzagLevelOrder(t1)
