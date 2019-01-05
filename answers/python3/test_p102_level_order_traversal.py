# coding: utf-8

__author__ = '代码会说话'
"""
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
from tree_node import  *
from typing import List

class Solution:
  def zigzagLevelOrder(self, root:TreeNode) -> List[List[int]]:
    if not root:
      return []
    nodes = [root]
    root.level = 1
    result = []
    level_list = []
    prev_level = 0
    reverse = False
    def append_level_list():
      nonlocal  reverse
      if level_list:
        if reverse:
          level_list.reverse()
          result.append(level_list)
        else:
          result.append(level_list)
        reverse = not reverse
    while nodes:
      node = nodes.pop(0)
      level = node.level
      if level > prev_level:
        append_level_list()
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
    append_level_list()

    return result


def test():
  s = Solution()
  t1 = make_simple_tree(3,9, make_simple_tree(20,15,7))

  assert [
    [3],
    [20,9],
    [15,7]
  ] == s.zigzagLevelOrder(t1)


