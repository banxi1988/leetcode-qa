# coding: utf-8

__author__ = '代码会说话'

"""
给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。

一般来说，删除节点可分为两个步骤：

首先找到需要删除的节点；
如果找到了，删除它。
说明： 要求算法时间复杂度为 O(h)，h 为树的高度。

示例:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。

一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。

    5
   / \
  4   6
 /     \
2       7

另一个正确答案是 [5,2,6,null,4,null,7]。

    5
   / \
  2   6
   \   \
    4   7
"""

from tree_node import  *

class Solution:
  def deleteNode(self, root:TreeNode, key:int):
    # 分类讨论：1) 完备，2）不重复.
    if not root:
      return None
    def findReplacement(target:TreeNode):
      # 选择一个比 target 大的。当然也可以选择一个比它小的。
      # 也就是出门右拐，向左下走 /
      # bigger 是相对于 target 而言。
      prev = target
      bigger = target.right
      while bigger.left:
        prev = bigger
        bigger = bigger.left
      return prev,bigger

    def deleteLeafNode(parent:TreeNode, leaf:TreeNode):
      if parent.left == leaf:
        parent.left = None
      if parent.right == leaf:
        parent.right = None

    def deleteBranchWithOneChild(parent:TreeNode,branch:TreeNode):
      if parent.left == branch:
        parent.left = branch.left if branch.left else branch.right
      else:
        parent.right = branch.left if branch.left else branch.right

    def deleteBranchWithTwoChild(branch:TreeNode):
      # 换值再删除另一个节点
      prev,replacement = findReplacement(branch)
      branch.val = replacement.val
      if replacement.left or replacement.right:
        # 这我们的这个场景下其实最多 replacement.right 可能为真。
        # 如果是找一个稍小的替代值的话，最多 replacement.left 可能为真
        deleteBranchWithOneChild(prev,replacement)
      else:
        deleteLeafNode(prev, replacement)

    def deleteRootNode(root:TreeNode):
      if root.left and root.right:
        deleteBranchWithTwoChild(root)
        return root
      elif root.left:
        return root.left
      elif root.right:
        return root.right
      else:
        return None

    parent = None
    target = root
    while target:
      if target.val == key:
        break
      elif target.val < key:
        parent = target
        target = target.right
      else:
        parent = target
        target = target.left
    if not target:
      return root
    if parent:
      if (target.left and target.right):
        deleteBranchWithTwoChild(target)
      elif target.left or target.right:
        deleteBranchWithOneChild(parent,target)
      else:
        deleteLeafNode(parent, target)
      return root
    else:
      return deleteRootNode(root)


def test():
  s = Solution()
  t1 = make_simple_tree(5, make_simple_tree(3,2,4), make_simple_tree(6,None,7))
  t1r = s.deleteNode(t1, 3)
  assert levelVisit(t1r) == [5,4,6,2,7]
  t2 = make_simple_tree(5, make_simple_tree(3,2,4), make_simple_tree(6,None,7))
  t2r = s.deleteNode(t2, 4)
  assert levelVisit(t2r) == [5,3,6,2,7]
  t3 = make_simple_tree(5, make_simple_tree(3,2,4), make_simple_tree(6,None,7))
  t3r = s.deleteNode(t3, 2)
  assert levelVisit(t3r) == [5,3,6,4,7]

  t4 = make_simple_tree(5, make_simple_tree(3,2,4), make_simple_tree(6,None,7))
  t4r = s.deleteNode(t4, 5)
  assert levelVisit(t4r) == [6,3,7,2,4]

  t5 = make_simple_tree(5, make_simple_tree(3,2,4), make_simple_tree(6,None,7))
  t5r = s.deleteNode(t5, 6)
  assert levelVisit(t5r) == [5,3,7,2,4]

  t6 = make_simple_tree(5, make_simple_tree(3,2,4), make_simple_tree(6,None,7))
  t6r = s.deleteNode(t6, 7)
  assert levelVisit(t6r) == [5,3,6,2,4]




