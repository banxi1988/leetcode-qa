# coding: utf-8

__author__ = '代码会说话'

"""
给你一个二叉树的根节点 root。设根节点位于二叉树的第 1 层，而根节点的子节点位于第 2 层，依此类推。

请你找出层内元素之和 最大 的那几层（可能只有一层）的层号，并返回其中 最小 的那个。

 

示例：



输入：[1,7,0,7,-8,null,null]
输出：2
解释：
第 1 层各元素之和为 1，
第 2 层各元素之和为 7 + 0 = 7，
第 3 层各元素之和为 7 + -8 = -1，
所以我们返回第 2 层的层号，它的层内元素之和最大。
 

提示：

树中的节点数介于 1 和 10^4 之间
-10^5 <= node.val <= 10^5
"""

from typing import List
from functools import lru_cache
from tree_node import *

from collections import defaultdict, Counter
class Solution:
  def maxLevelSum(self, root: TreeNode) -> int:
    nodes = [root]
    root.level = 1
    level_to_sum = defaultdict(int)
    while nodes:
      branch = nodes.pop()
      level = branch.level
      level_to_sum[level] += branch.val
      left = branch.left
      right = branch.right
      if left:
        left.level = level + 1
        nodes.append(left)
      if right:
        right.level = level + 1
        nodes.append(right)

    level_sum_pairs = []
    for level,sum in level_to_sum.items():
      level_sum_pairs.append((sum,level))

    level_sum_pairs.sort(reverse=True, key=lambda item: (item[0],-item[1]))

    return level_sum_pairs[0][1]



def test():
  s = Solution()
  t1 = make_simple_tree(1,make_simple_tree(7,7,-8),0)

  assert s.maxLevelSum(t1) == 2
  t2 = make_simple_tree(1,make_simple_tree(7,7,0),0)
  assert s.maxLevelSum(t2) == 2
