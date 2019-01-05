# coding: utf-8

__author__ = '代码会说话'
"""
给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

例如:
给定二叉树: [3,9,20,null,null,15,7],

   3
  / \
  9  20
    / \
  15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
"""
from tree_node import  *
from typing import List

from collections import defaultdict

class Solution:
  def levelOrder(self, root:TreeNode) -> List[List[int]]:
    if not root:
      return []
    nodes = [root]
    root.level = 1
    result = []
    level_list = []
    prev_level = 0
    while nodes:
      node = nodes.pop(0)
      level = node.level
      if level > prev_level:
        if level_list:
          result.append(level_list)
        level_list = []
        prev_level = level
      level_list.append(node.val)
      left = node.left
      right = node.right

      if left:
        left.level = level + 1
        nodes.append(left)
      if right:
        right.level = level + 1
        nodes.append(right)

    if level_list:
      result.append(level_list)

    return result


def test():
  s = Solution()
  t1 = make_simple_tree(3,9, make_simple_tree(20,15,7))

  assert [
    [3],
    [9,20],
    [15,7]
  ] == s.levelOrder(t1)


