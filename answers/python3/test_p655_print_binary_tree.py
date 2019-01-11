# coding: utf-8

__author__ = '代码会说话'
"""
在一个 m*n 的二维字符串数组中输出二叉树，并遵守以下规则：

行数 m 应当等于给定二叉树的高度。
列数 n 应当总是奇数。
根节点的值（以字符串格式给出）应当放在可放置的第一行正中间。根节点所在的行与列会将剩余空间划分为两部分（左下部分和右下部分）。你应该将左子树输出在左下部分，右子树输出在右下部分。左下和右下部分应当有相同的大小。即使一个子树为空而另一个非空，你不需要为空的子树输出任何东西，但仍需要为另一个子树留出足够的空间。然而，如果两个子树都为空则不需要为它们留出任何空间。
每个未使用的空间应包含一个空的字符串""。
使用相同的规则输出子树。

2^n -1
示例 1:

输入:
     1
    /
   2
输出:
[["", "1", ""],
 ["2", "", ""]]
示例 2:

输入:
     1
    / \
   2   3
    \
     4
输出:
[["", "", "", "1", "", "", ""],  (cols + 1)/2 = 4
 ["", "2", "", "", "", "3", ""],  = 2 + 2 * 2
 ["", "", "4", "", "", "", ""]]  1  , 1 + 1 *2
示例 3:

输入:
      1
     / \
    2   5
   / 
  3 
 / 
4 
输出:
[["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""] 16 /2 = 8
 ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""] 16/4  = 4, 4 + 4*2 = 12
 ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
 ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]
注意: 二叉树的高度在范围 [1, 10] 中。



"""

from tree_node import  *

from collections import deque
class Solution:
  def printTree(self, root:TreeNode) -> List[List[str]]:
    if not root:
      return []
    root.no = 1
    root.level = 1
    rows = depthOfTree(root)
    cols = pow(2,rows) -1
    grids = [[''] * cols for _ in range(0,rows)]
    nodes = deque()
    nodes.append(root)
    while nodes:
      node = nodes.popleft()
      no = node.no
      level = node.level
      step = (cols + 1) // pow(2,level)
      start_no = pow(2, level -1)
      col_no = no - start_no + 1
      col = step * (2*col_no - 1)
      grids[level -1][col-1] = str(node.val)

      left = node.left
      if left:
        left.no = 2*no
        left.level = level + 1
        nodes.append(left)
      right = node.right
      if right:
        right.no = 2*no + 1
        right.level = level + 1
        nodes.append(right)
    return grids


def test():
  s = Solution()
  t1 = make_simple_tree(1,2,None)

  assert s.printTree(t1) == [["", "1", ""],
                             ["2", "", ""]]

  t2 = make_simple_tree(1,2,3)
  t2.left.right = TreeNode(4)

  # 7:4
  # 7: 2,6
  assert s.printTree(t2) == [["", "", "", "1", "", "", ""],
                             ["", "2", "", "", "", "3", ""],
                             ["", "", "4", "", "", "", ""]]

  t3 = make_flat_tree([1,2,3,4])
  t3.right = TreeNode(5)
  assert s.printTree(t3) == [["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""],
                             ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""],
                             ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""],
                             ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
                             ]