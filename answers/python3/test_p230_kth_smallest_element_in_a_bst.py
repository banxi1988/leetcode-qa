# coding: utf-8

__author__ = '代码会说话'

"""
给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。

说明：
你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。

示例 1:

输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 1
示例 2:

输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 3
进阶：
如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化 kthSmallest 函数？


"""

from tree_node import  *

class Solution:
  def kthSmallest(self, root:TreeNode, k:int) -> int:
    generator = bst_generator(root)
    i = 1
    while i < k:
      next(generator)
      i+=1
    return next(generator).val




def test():
  s = Solution()
  t1 = make_simple_tree(3,make_simple_tree(1,None,2), 4)
  assert s.kthSmallest(t1, 1) == 1

  t2 = make_simple_tree(3, make_simple_tree(3,make_simple_tree(2,1,None),4), 6)
  assert s.kthSmallest(t2, 3) == 3

