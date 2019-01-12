# coding: utf-8

__author__ = '代码会说话'
"""
给出一个完全二叉树，求出该树的节点个数。

说明：

完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。

示例:

输入: 
    1
   / \
  2   3
 / \  /
4  5 6

输出: 6
"""

from tree_node import *

from collections import deque
class Solution:
  def countNodes(self, root:TreeNode) -> int:
    if not root:
      return 0
    nodes = deque()
    nodes.append(root)
    count = 0
    while nodes:
      node = nodes.popleft()
      count += 1
      left = node.left
      right = node.right
      if left:
        nodes.append(left)
      if right:
        nodes.append(right)
    return count

def test():
  s = Solution()

  t1 = make_simple_tree(1,make_simple_tree(2,4,5), make_simple_tree(3,6,None))
  assert s.countNodes(t1) == 6
  t2 = make_simple_tree(1,make_simple_tree(2,4,None), 3)
  assert s.countNodes(t2) == 4
