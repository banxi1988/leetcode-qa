# coding: utf-8

__author__ = '代码会说话'

"""
给定一个二叉树，确定它是否是一个完全二叉树。

百度百科中对完全二叉树的定义如下：

若设二叉树的深度为 h，除第 h 层外，其它各层 (1～h-1) 的结点数都达到最大个数，第 h 层所有的结点都连续集中在最左边，这就是完全二叉树。（注：第 h 层可能包含 1~ 2h 个节点。）


"""


# Definition for a binary tree node.
from tree_node import *
from collections import deque
class Solution:
  def isCompleteTree(self, root:TreeNode) -> bool:
    if not root:
      return True
    nodes = deque()
    nodes.append(root)
    prev = 0
    root.no = 1
    while len(nodes):
      node = nodes.popleft()
      no = node.no
      if prev + 1 != no:
        return False
      prev = no
      left = node.left
      right = node.right
      if left:
        left.no = 2 * no
        nodes.append(left)
      if right:
        right.no = 2* no + 1
        nodes.append(right)
    return True




def test():
  s = Solution()
  t1 = make_simple_tree(1,make_simple_tree(2,4,5),make_simple_tree(3,6,None))
  assert s.isCompleteTree(t1)

  t2 = make_simple_tree(1,make_simple_tree(2,4,5),make_simple_tree(3,None,7))
  assert s.isCompleteTree(t2) == False
