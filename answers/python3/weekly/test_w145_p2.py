# coding: utf-8

__author__ = '代码会说话'

"""
给你一个有根节点的二叉树，找到它最深的叶节点的最近公共祖先。

回想一下：

叶节点 是二叉树中没有子节点的节点
树的根节点的 深度 为 0，如果某一节点的深度为 d，那它的子节点的深度就是 d+1
如果我们假定 A 是一组节点 S 的 最近公共祖先，s 中的每个节点都在以 A 为根节点的子树中，且 A 的深度达到此条件下可能的最大值。
 

示例 1：

输入：root = [1,2,3]
输出：[1,2,3]
示例 2：

输入：root = [1,2,3,4]
输出：[4]
示例 3：

输入：root = [1,2,3,4,5]
输出：[2,4,5]
 

提示：

给你的树中将有 1 到 1000 个节点。
树中每个节点的值都在 1 到 1000 之间。
"""

from typing import List
from functools import lru_cache
from collections import defaultdict, Counter
from tree_node import *

class Solution:
  def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
    level_to_nodes = defaultdict(list)
    level_to_nodes[0] = [root]
    level = 0
    while True:
      nodes = level_to_nodes[level]
      if len(nodes) < 1:
        break
      next_level = level + 1
      for node in nodes:
        left = node.left
        right = node.right
        if left:
          left.parent = node
          level_to_nodes[next_level].append(left)
        if right:
          right.parent = node
          level_to_nodes[next_level].append(right)
      level = next_level

    max_level = level - 1
    deepest_nodes = level_to_nodes[max_level]
    if len(deepest_nodes) == 1:
      return deepest_nodes[0]
    parent_set = set(deepest_nodes)
    while len(parent_set) > 1:
      parent_set = {node.parent for node in parent_set}

    return parent_set.pop()




def test():
  s = Solution()
  t3 = make_simple_tree(1,make_simple_tree(2,4,5), 3)
  assert s.lcaDeepestLeaves(t3) == make_simple_tree(2,4,5)

  t1 = make_simple_tree(1,2,3)
  assert s.lcaDeepestLeaves(t1) == t1
  t2 = make_simple_tree(1, make_simple_tree(2,4,None), 3)
  assert s.lcaDeepestLeaves(t2) == TreeNode(4)
