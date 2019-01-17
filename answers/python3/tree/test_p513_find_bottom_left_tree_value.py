# coding: utf-8

__author__ = '代码会说话'

"""
给定一个二叉树，在树的最后一行找到最左边的值。

示例 1:

输入:

    2
   / \
  1   3

输出:
1
 

示例 2:

输入:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

输出:
7
 

注意: 您可以假设树（即给定的根节点）不为 NULL。
"""

from tree_node import *


class Solution:
  def findBottomLeftValue(self, root:TreeNode) -> int:
    prev_nodes = [root]
    while True:
      next_nodes = []
      for node in prev_nodes:
        left = node.left
        right = node.right
        if left:
          next_nodes.append(left)
        if right:
          next_nodes.append(right)
      if next_nodes:
        prev_nodes = next_nodes
      else:
        break

    return prev_nodes[0].val


def test():
  s = Solution()
  t1 = make_simple_tree(2,1,3)
  assert s.findBottomLeftValue(t1) == 1

  t2 = make_flat_tree([1,2,4])
  t2.right = make_simple_tree(3,5,6)
  t2.find_child_node_by_val(5).left = TreeNode(7)

  assert s.findBottomLeftValue(t2) == 7


