# coding: utf-8

__author__ = '代码会说话'
"""

"""

from tree_node import  *

from typing import Optional
class Solution:
  def pruneTree(self, root:TreeNode) -> Optional[TreeNode]:
    if not root:
      return None
    def prune(root:TreeNode)-> Optional[TreeNode]:
      if root.left:
        root.left = prune(root.left)
      if root.right:
        root.right = prune(root.right)
      if  root.left or root.right:
          return root
      return root if root.val == 1 else None

    return prune(root)



def test():
  s = Solution()
  t1 = TreeNode(1)
  t1.right = make_simple_tree(0,0,1)
  t1r = s.pruneTree(t1)
  assert levelVisit(t1r) == [1,0,1]
