# coding: utf-8

__author__ = '代码会说话'

"""
给定一个二叉树，原地将它展开为链表。

例如，给定二叉树

    1
   / \
  2   5
 / \   \
3   4   6
   /
  7
将其展开为：

N: 1,4,7,
p:3

p->right


1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""

from tree_node import *

class Solution:
  def flatten(self, root:TreeNode):
    if not root:
      return
    link_node = None
    left_most = []
    def collect_left_most(branch:TreeNode):
      nonlocal link_node
      if link_node:
        link_node.left = branch
      p = branch
      while p:
        left_most.append(p)
        p = p.left
      link_node = left_most[-1]
    collect_left_most(root)
    while left_most:
      node = left_most.pop()
      if node.right:
        collect_left_most(node.right)
        node.right = None

    p = root
    while p:
      left = p.left
      p.right = left
      p.left = None
      p = left



def test():
  s = Solution()
  t1 = make_simple_tree(1,make_simple_tree(2,3,4), make_simple_tree(5,None,6))
  s.flatten(t1)
  nums = levelVisit(t1)
  assert [1,2,3,4,5,6] == nums


