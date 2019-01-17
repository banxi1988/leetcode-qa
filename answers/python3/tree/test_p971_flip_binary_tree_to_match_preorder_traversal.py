# coding: utf-8

__author__ = '代码会说话'
"""
给定一个有 N 个节点的二叉树，每个节点都有一个不同于其他节点且处于 {1, ..., N} 中的值。

通过交换节点的左子节点和右子节点，可以翻转该二叉树中的节点。

考虑从根节点开始的先序遍历报告的 N 值序列。将这一 N 值序列称为树的行程。

（回想一下，节点的先序遍历意味着我们报告当前节点的值，然后先序遍历左子节点，再先序遍历右子节点。）

我们的目标是翻转最少的树中节点，以便树的行程与给定的行程 voyage 相匹配。 

如果可以，则返回翻转的所有节点的值的列表。你可以按任何顺序返回答案。

如果不能，则返回列表 [-1]。

 

示例 1：



输入：root = [1,2], voyage = [2,1]
输出：[-1]
示例 2：



输入：root = [1,2,3], voyage = [1,3,2]
输出：[1]
示例 3：



输入：root = [1,2,3], voyage = [1,2,3]
输出：[]
 

提示：

1 <= N <= 100

    2
  1   4 
5    3
"""

from tree_node import  *

from typing import List
class Solution:
  def flip(self, root:TreeNode, voyage:List[int],fliped:List[int]):
    if bool(root) != bool(voyage):
      raise Exception("cnnot flip")
    if not root:
      return

    vm = voyage.pop(0)
    if root.val != vm:
      raise Exception("cannot flip")
    left = root.left
    right = root.right
    if left and right:
      lv_index = voyage.index(left.val)
      rv_index = voyage.index(right.val)
      if lv_index < rv_index:
        self.flip(left,voyage, fliped)
        self.flip(right,voyage, fliped)
      else:
        fliped.append(root.val)
        self.flip(right,voyage, fliped)
        self.flip(left,voyage, fliped)
    elif left:
      vl = voyage[0]
      if left.val != vl:
        raise Exception("cannot flip")
      self.flip(left, voyage, fliped)
    elif right:
      vr = voyage[0]
      if right.val != vr:
        raise Exception("cannot flip")
      self.flip(right, voyage, fliped)


  def flipMatchVoyage(self, root:TreeNode, voyage:List[int]) -> List[int]:
    fliped = []
    try:
      self.flip(root, voyage, fliped)
      if len(voyage)  > 0:
        return [-1]
    except:
      return [-1]
    else:
      return fliped


def test():
  s = Solution()
  t5 = make_simple_tree(2,make_simple_tree(5,6,None),make_simple_tree(3,make_simple_tree(4,None,1), None))
  assert [2,5,3,6,4,1] == levelVisit(t5)
  assert s.flipMatchVoyage(t5,[2,5,6,3,4,1]) == []
  t4 = make_simple_tree(2, make_simple_tree(1,5,None)
                        ,make_simple_tree(4,3,None))

  assert [2,1,4,5,3] == levelVisit(t4)

  assert [2] == s.flipMatchVoyage(t4,[2,4,3,1,5])

  t1 = make_simple_tree(1,2, None)
  assert [-1] == s.flipMatchVoyage(t1, [2,1])

  t2 = make_simple_tree(1,2,3)
  assert [1] == s.flipMatchVoyage(t2,[1,3,2])

  t3 = make_simple_tree(1,2,3)
  assert [] == s.flipMatchVoyage(t3,[1,2,3])


"""
   2
  5   3
6  n 4 n
      \
       1
[2,5,3,6,null,4,null,null,null,null,1]
[2,5,6,3,4,1]
输出：
[-1]
预期：
[]
"""