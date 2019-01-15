# coding: utf-8

__author__ = '代码会说话'
"""
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
 pre: 1,2,3,4,2,4,3
spre: 1,2,3,4,2,4,3

但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
 pre: 1,2,null,3,2,null,3
spre: 1,2,3,null,,2,3 
说明:

如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
"""

from tree_node import *



class Solution:
  def isSymmetric(self, root:TreeNode) -> bool:
    if not root:
      return True
    def is_same_symmetric_preorder(left:TreeNode,right:TreeNode)->bool:
      if left and right:
        if left.val != right.val:
          return False
        return is_same_symmetric_preorder(left.left, right.right) and is_same_symmetric_preorder(left.right,right.left)
      elif left or right:
        return False
      else:
        return True
    return is_same_symmetric_preorder(root.left,root.right)