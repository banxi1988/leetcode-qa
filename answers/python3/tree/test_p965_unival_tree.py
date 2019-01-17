# coding: utf-8

__author__ = '代码会说话'


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x:int):
        self.val = x
        self.left = None # type: TreeNode
        self.right = None # type: TreeNode

class Solution:
  def isUnivalTree(self, root:TreeNode) -> bool: #
    target = root.val
    branches = [root]
    while branches:
      branch = branches.pop(0)
      if branch.val != target:
        return False
      if branch.left:
        branches.append(branch.left)
      if branch.right:
        branches.append(branch.right)
    return True

