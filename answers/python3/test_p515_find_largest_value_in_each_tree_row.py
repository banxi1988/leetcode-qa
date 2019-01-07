# coding: utf-8

__author__ = '代码会说话'

"""
您需要在二叉树的每一行中找到最大的值。

示例：

输入: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

输出: [1, 3, 9]
"""

from tree_node import *

class Solution:
  def largestValues(self, root:TreeNode) -> List[int]:
    if not root:
      return []
    values_list = levelOrder(root)
    return [max(values) for values in values_list]


def test():
  s = Solution()
  t1 = make_simple_tree(1,make_simple_tree(3,5,3), make_simple_tree(2,None,9))
  assert [1,3,9] == s.largestValues(t1)
