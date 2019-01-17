# coding: utf-8

__author__ = '代码会说话'

"""
给定一个不含重复元素的整数数组。一个以此数组构建的最大二叉树定义如下：

二叉树的根是数组中的最大元素。
左子树是通过数组中最大值左边部分构造出的最大二叉树。
右子树是通过数组中最大值右边部分构造出的最大二叉树。
通过给定的数组构建最大二叉树，并且输出这个树的根节点。

Example 1:

输入: [3,2,1,6,0,5]
输入: 返回下面这棵树的根节点：

         6  
    /        \
   3          5
    \         / 
     2       0   
       \
        1
注意:

给定的数组的大小在 [1, 1000] 之间。
"""

from tree_node import  *

def find_max(nums:List[int]):
  max_num = nums[0]
  max_index = 0
  for index,num in enumerate(nums):
    if num > max_num:
      max_num = num
      max_index = index

  return max_index,max_num

class Solution:
  def constructMaximumBinaryTree(self, nums:List[int]):
    if not nums:
      return None
    max_index,max_num = find_max(nums)
    root = TreeNode(max_num)
    root.left = self.constructMaximumBinaryTree(nums[:max_index])
    root.right = self.constructMaximumBinaryTree(nums[max_index +1:])
    return root

def test():
  s = Solution()
  t1 = s.constructMaximumBinaryTree([3,2,1,6,0,5])

  assert levelVisit(t1) == [6,3,5,2,0,1]