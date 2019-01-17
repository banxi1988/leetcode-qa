# coding: utf-8

__author__ = '代码会说话'

"""
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""

from tree_node import *

class Solution:
  def pathSum(self, root:TreeNode, sum:int) -> List[List[int]]:
    if not root:
      return []
    nodes = [root]
    root.sum = root.val
    node_to_path = {root: [root.val]}
    results = []
    def collect_node(node:TreeNode,parent_sum:int,parent_path:List[int]):
      sum = node.val + parent_sum
      node.sum = sum
      node_path = list(parent_path)
      node_path.append(node.val)
      node_to_path[node] = node_path
      nodes.append(node)

    while nodes:
      node = nodes.pop()
      left = node.left
      right = node.right
      node_sum = node.sum
      node_path = node_to_path[node]
      if not (left or right):
        if node_sum == sum:
          results.append(node_path)
      else:
        if left:
          collect_node(left, node_sum, node_path)
        if right:
          collect_node(right, node_sum, node_path)

    return results

def test_path_sum(benchmark):
  s = Solution()
  t1 = make_simple_tree(5,4,make_simple_tree(8,13,make_simple_tree(4,5,1)))
  t1.left.left = make_simple_tree(11,7,2)
  n13 = t1.find_child_node_by_val(13)
  n7 = t1.find_child_node_by_val(7)
  n13.left = make_basic_tree()
  n13.right = make_basic_tree()
  n7.left = make_basic_tree()
  n7.right = make_basic_tree()

  r1 = benchmark(s.pathSum, t1,22)
  assert r1 == [
    [5,8,4,5],
    [5,4,11,2]
  ]
