# coding: utf-8

__author__ = '代码会说话'

from tree_node import  *
from typing import List

def bt_inorder_generator(root:TreeNode):
  left_most = []
  def collect_left_most(node:TreeNode):
    p = node
    while p:
      left_most.append(p)
      p = p.left

  collect_left_most(root)
  while left_most:
    node = left_most.pop()
    yield node
    if node.right:
      collect_left_most(node.right)

class Solution:
  def inorderTraversal(self, root:TreeNode)->List[int]:
    if not root:
      return []
    gen = bt_inorder_generator(root)
    return [node.val for node in gen]


def test():
  s = Solution()
  t1 = make_simple_tree(1,None,make_simple_tree(2,3,None))

  assert [1,3,2] == s.inorderTraversal(t1)


