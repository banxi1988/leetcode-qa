# coding: utf-8

__author__ = '代码会说话'

from tree_node import *

class Solution:
  def sumRootToLeaf(self, root: TreeNode) -> int:
    M = pow(10,9) + 7
    root.num = str(root.val)
    nodes = [root]
    ans = 0
    while nodes:
      branch = nodes.pop()
      left = branch.left
      right = branch.right
      pnum = branch.num
      if left or right:
        if left:
          left.num = pnum + str(left.val)
          nodes.append(left)
        if right:
          right.num = pnum + str(right.val)
          nodes.append(right)
      else:
        num = int(pnum,2) % M
        ans += num
        ans %= M
    return ans





def test():
  s = Solution()
  t1 = make_simple_tree(1,make_simple_tree(0,0,1),make_simple_tree(1,0,1))
  assert s.sumRootToLeaf(t1) == 22

  assert s.sumRootToLeaf(make_simple_tree(1,None,None)) == 1
  assert s.sumRootToLeaf(make_simple_tree(0,None,None)) == 0
