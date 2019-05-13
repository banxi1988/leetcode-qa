# coding: utf-8

__author__ = '代码会说话'

from tree_node import *


class Solution:
  def maxAncestorDiff(self, root: TreeNode) -> int:
    nodes = []

    def add_start_node(node: TreeNode):
      node.parent_max = root.val
      node.parent_min = root.val
      node.parent = root
      nodes.append(node)

    if root.left:
      add_start_node(root.left)
    if root.right:
      add_start_node(root.right)

    def add_node(node: TreeNode, parent: TreeNode):
      node.parent_max = max(parent.val, parent.parent_max)
      node.parent_min = min(parent.val, parent.parent_min)
      nodes.append(node)

    max_diff = 0
    while nodes:
      parent = nodes.pop()
      diff1 = abs(parent.parent_max - parent.val)
      diff2 = abs(parent.parent_min - parent.val)
      max_diff = max(diff1, diff2, max_diff)
      if parent.left:
        add_node(parent.left, parent)
      if parent.right:
        add_node(parent.right, parent)
    return max_diff


def test():
  s = Solution()
  codec = Codec()
  t3 = codec.deserialize("[1,null,2,null,0,3]")
  assert s.maxAncestorDiff(t3) == 3
  t2 = codec.deserialize("[2,null,0,1]")
  assert s.maxAncestorDiff(t2) == 2
  t1 = codec.deserialize("[8,3,10,1,6,null,14,null,null,4,7,13]")
  assert s.maxAncestorDiff(t1) == 7
