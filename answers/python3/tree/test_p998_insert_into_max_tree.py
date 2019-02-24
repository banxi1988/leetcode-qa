# coding: utf-8

__author__ = '代码会说话'

"""
998. 最大二叉树 II

最大树定义：一个树，其中每个节点的值都大于其子树中的任何其他值。

给出最大树的根节点 root。

就像之前的问题那样，给定的树是从表 A（root = Construct(A)）递归地使用下述 Construct(A) 例程构造的：

如果 A 为空，返回 null
否则，令 A[i] 作为 A 的最大元素。创建一个值为 A[i] 的根节点 root
root 的左子树将被构建为 Construct([A[0], A[1], ..., A[i-1]])
root 的右子树将被构建为 Construct([A[i+1], A[i+2], ..., A[A.length - 1]])
返回 root
请注意，我们没有直接给定 A，只有一个根节点 root = Construct(A).

假设 B 是 A 的副本，并附加值 val。保证 B 中的值是不同的。

返回 Construct(B)。
"""

from tree_node import *

class Solution:
  def insertIntoMaxTree(self, root: 'TreeNode', val: 'int') -> 'TreeNode':
    if val > root.val:
      newRoot = TreeNode(val)
      newRoot.left = root
      return newRoot
    if root.right:
      root.right = self.insertIntoMaxTree(root.right, val)
      return root
    else:
      root.right = TreeNode(val)
    return root

def test():
  s = Solution()
  codec = Codec()

  t0 = codec.deserialize("[3,2]")
  t0_r = s.insertIntoMaxTree(t0,1)
  assert codec.serialize(t0_r) == "[3,2,1]"

  t1 = codec.deserialize("[4,1,3,null,null,2]")
  t1_r = s.insertIntoMaxTree(t1, 5)
  assert codec.serialize(t1_r) == "[5,4,null,1,3,null,null,2]"

  t2 = codec.deserialize("[5,2,4,null,1]")
  t2_r = s.insertIntoMaxTree(t2,3)
  assert codec.serialize(t2_r) == "[5,2,4,null,1,null,3]"

  t3 = codec.deserialize("[5,2,3,null,1]")
  t3_r = s.insertIntoMaxTree(t3,4)
  assert codec.serialize(t3_r) == "[5,2,4,null,1,3]"


