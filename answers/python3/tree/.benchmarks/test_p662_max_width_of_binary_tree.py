# coding: utf-8

__author__ = '代码会说话'

"""
给定一个二叉树，编写一个函数来获取这个树的最大宽度。树的宽度是所有层中的最大宽度。这个二叉树与满二叉树（full binary tree）结构相同，但一些节点为空。

每一层的宽度被定义为两个端点（该层最左和最右的非空节点，两端点间的null节点也计入长度）之间的长度。

示例 1:

输入: 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

输出: 4
解释: 最大值出现在树的第 3 层，宽度为 4 (5,3,null,9)。
示例 2:

输入: 

          1
         /  
        3    
       / \       
      5   3     

输出: 2
解释: 最大值出现在树的第 3 层，宽度为 2 (5,3)。
示例 3:

输入: 

          1
         / \
        3   2 
       /        
      5      

输出: 2
解释: 最大值出现在树的第 2 层，宽度为 2 (3,2)。
示例 4:

输入: 

          1
         / \
        3   2
       /     \  
      5       9 
     /         \
    6           7
输出: 8
解释: 最大值出现在树的第 4 层，宽度为 8 (6,null,null,null,null,null,null,7)。
注意: 答案在32位有符号整数的表示范围内。
"""

from tree_node import *

from collections import namedtuple, defaultdict
class LevelNoRange:
  __slots__ = ('min', 'max')
  def __init__(self):
    self.min = 0
    self.max = 0

class Solution:
  def widthOfBinaryTree_index(self, root:TreeNode) -> int:
    if not root:
      return 0
    nodes = [root]
    root.level = 1
    root.no = 1
    level_to_range = defaultdict(LevelNoRange)
    max_width = 1
    while nodes:
      node = nodes.pop()
      level = node.level
      no = node.no
      left = node.left
      right = node.right
      r = level_to_range[level]
      if r.min == 0:
        r.min = no
      if r.max == 0:
        r.max = no
      r.min = min(r.min, no)
      r.max = max(r.max, no)
      if left:
        left.level = level + 1
        left.no =  2 * no
        nodes.append(left)
      if right:
        right.level  = level + 1
        right.no = 2 * no + 1
        nodes.append(right)
      width = r.max - r.min + 1
      max_width = max(max_width, width)

    return max_width

  def widthOfBinaryTree_level(self, root:TreeNode) -> int:
    if not root:
      return 0
    root.level = 1
    max_width = 1
    prev_level_symbols = [root]
    while True:
      new_level_symbols = []
      for symbol in prev_level_symbols:
        left = None
        right = None
        if symbol:
          left = symbol.left
          right = symbol.right
        if new_level_symbols or left:
          new_level_symbols.append(left)
          new_level_symbols.append(right)
        elif right:
          new_level_symbols.append(right)
      end_index = len(new_level_symbols)
      while end_index > 0 and new_level_symbols[end_index-1] is None:
        end_index -= 1
      if end_index < 1:
        break
      level_symbols = new_level_symbols[:end_index]
      prev_level_symbols = level_symbols
      max_width = max(max_width, len(level_symbols))
    return max_width

  widthOfBinaryTree = widthOfBinaryTree_index



def test_width_of_binary_tree():
  s = Solution()
  t1 = make_flat_tree([1,2,9], left_leaning=False)
  t1.left = make_simple_tree(3,5,3)
  assert levelVisit(t1) == [1,3,2,5,3,9]

  assert s.widthOfBinaryTree(t1) == 4
  t2 = TreeNode(1)
  t2.left = make_simple_tree(3,5,3)
  assert s.widthOfBinaryTree(t2) == 2

  t3 = make_simple_tree(1,3,2)
  t3.left.left = TreeNode(5)
  assert s.widthOfBinaryTree(t3) == 2

  t4 = make_flat_tree([1,3,5,6])
  t4.right = make_flat_tree([2,9,7], left_leaning=False)
  assert s.widthOfBinaryTree(t4) == 8

