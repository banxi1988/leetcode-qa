# coding: utf-8

__author__ = '代码会说话'

"""
LeetCode 95. 不同的二叉搜索树 II by 代码会说话
给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。

示例:

输入: 3
输出:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释:
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

def test():
    s = Solution()
    assert s.generateTrees(3) == [
        [1,None,3,2],
        [3,2,None,1],
        [3,1,None,None,2],
        [2,1,3],
        [1,None,2,None,3]
    ]
