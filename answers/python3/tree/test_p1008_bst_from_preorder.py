# coding: utf-8

__author__ = '代码会说话'

from tree_node import *

"""
1 <= preorder.length <= 100
先序 preorder 中的值是不同的。
"""

import bisect


class Solution:
  def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
    N = len(preorder)
    if N == 1:
      return TreeNode(preorder[0])
    if N == 2:
      root = TreeNode(preorder[0])
      root.left = TreeNode(preorder[1])
    root_val = preorder[0]
    root = TreeNode(root_val)
    index = bisect.bisect_left(preorder, root_val, lo=1)
    left_preorder = preorder[1:index]
    right_preorder = preorder[index:]
    if left_preorder:
      root.left = self.bstFromPreorder(left_preorder)
    if right_preorder:
      root.right = self.bstFromPreorder(right_preorder)

    return root


def test():
  codec = Codec()
  s = Solution()
  t1 = s.bstFromPreorder(preorder=[8, 5, 1, 7, 10, 12])
  assert codec.serialize(t1) == "[8,5,10,1,7,null,12]"
