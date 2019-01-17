# coding: utf-8

__author__ = '代码会说话'
"""
给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。

例如，从根到叶子节点路径 1->2->3 代表数字 123。

计算从根到叶子节点生成的所有数字之和。

说明: 叶子节点是指没有子节点的节点。

示例 1:

输入: [1,2,3]
    1
   / \
  2   3
输出: 25
解释:
从根到叶子节点路径 1->2 代表数字 12.
从根到叶子节点路径 1->3 代表数字 13.
因此，数字总和 = 12 + 13 = 25.
示例 2:

输入: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
输出: 1026
解释:
从根到叶子节点路径 4->9->5 代表数字 495.
从根到叶子节点路径 4->9->1 代表数字 491.
从根到叶子节点路径 4->0 代表数字 40.
因此，数字总和 = 495 + 491 + 40 = 1026.
"""

from tree_node import *

class Solution:
  def sumNumbers(self, root:TreeNode) -> int:
    if not root:
      return 0
    nodes = [root]
    root.num = root.val
    nums = []
    while nodes:
      node = nodes.pop(0)
      num = node.num
      left = node.left
      right = node.right
      if left or right:
        if left:
          left.num = num * 10 + left.val
          nodes.append(left)
        if right:
          right.num = num * 10 + right.val
          nodes.append(right)
      else:
        nums.append(num)

    return sum(nums)



def test():
  s = Solution()
  t1 = make_simple_tree(1,2,3)
  assert s.sumNumbers(t1) == 25

  t2 = make_simple_tree(4,make_simple_tree(9,5,1), 0)
  assert s.sumNumbers(t2) == 1026

  t3 = make_simple_tree(0,1,None)
  assert s.sumNumbers(t3) == 1
