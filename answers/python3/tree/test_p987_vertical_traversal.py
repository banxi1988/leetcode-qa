# coding: utf-8

__author__ = '代码会说话'
"""
987. Vertical Order Traversal of a Binary Tree

Given a binary tree, return the vertical order traversal of its nodes values.

For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).

Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes, we report the values of the nodes in order from top to bottom (decreasing Y coordinates).

If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.

Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.

 

Example 1:



Input: [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation: 
Without loss of generality, we can assume the root node is at position (0, 0):
Then, the node with value 9 occurs at position (-1, -1);
The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
The node with value 20 occurs at position (1, -1);
The node with value 7 occurs at position (2, -2).
Example 2:



Input: [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation: 
The node with value 5 and the node with value 6 have the same position according to the given scheme.
However, in the report "[1,5,6]", the node value of 5 comes first since 5 is smaller than 6.
 

Note:

The tree will have between 1 and 1000 nodes.
Each node's value will be between 0 and 1000.

"""

from tree_node import *

from typing import List
from collections import defaultdict
class Point:
  def __init__(self,x:int,y:int,val:int):
    self.x = x
    self.y = y
    self.val = val

  def __str__(self):
    return "%d,%d=%d" % (self.x,self.y,self.val)

  def __repr__(self):
    return str(self)

class Solution:
  def verticalTraversal(self, root: 'TreeNode') -> 'List[List[int]]':
    if not root:
      return []
    points = []
    root.point = Point(1000,1000,root.val)
    nodes = [root]
    while nodes:
      node = nodes.pop()
      point = node.point
      points.append(point)
      left = node.left
      right = node.right
      if left:
        left.point = Point(point.x -1, point.y -1, left.val)
        nodes.append(left)
      if right:
        right.point = Point(point.x +1, point.y -1, right.val)
        nodes.append(right)
    x_to_points = defaultdict(list)
    for point in points:
      x_to_points[point.x].append(point)
    for _,points in x_to_points.items():
      points.sort(key=lambda p:(-p.y,p.val))
    results = []
    xlist = sorted(x_to_points.keys())
    for x in xlist:
      points = x_to_points[x]
      values = [p.val for p in points]
      results.append(values)
    return results


def test():
  s = Solution()
  t1 = make_simple_tree(3,9, make_simple_tree(20,15,7))
  assert s.verticalTraversal(t1) == [[9],[3,15],[20],[7]]

  t2 = make_simple_tree(1,make_simple_tree(2,4,5),make_simple_tree(3,6,7))
  assert s.verticalTraversal(t2) == [[4],[2],[1,5,6],[3],[7]]
