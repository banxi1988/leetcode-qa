# coding: utf-8

__author__ = '代码会说话'

"""
[LeetCode 1022]. 从根到叶的二进制数之和

给出一棵二叉树，其上每个结点的值都是 0 或 1 。每一条从根到叶的路径都代表一个从最高有效位开始的二进制数。
例如，如果路径为 0 -> 1 -> 1 -> 0 -> 1，那么它表示二进制数 01101，也就是 13 。

对树上的每一片叶子，我们都要找出从根到该叶子的路径所表示的数字。

以 10^9 + 7 为模，返回这些数字之和。

 

示例：
          1
      0       1
  0    1    0    1


输入：[1,0,1,0,1,0,1]
输出：22
解释：(100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
 
MOD  = 109
branch: 126
mod_branch: 126 % 109 = 17
leaf: 126 * 2 + 1 = 253 % 109 = 35
leaf: 17 * 2 + 1 = 35 % 109 = 35


提示：

树中的结点数介于 1 和 1000 之间。
node.val 为 0 或 1 。
"""

from tree_node import TreeNode,make_simple_tree

class Solution:
  def sumRootToLeaf(self, root: TreeNode) -> int:
    MOD = pow(10,9) + 7
    root.num = root.val
    ans = 0
    nodes = [root]
    while nodes:
      branch = nodes.pop()
      left = branch.left
      right = branch.right

      base_num = branch.num << 1 #

      if left is None and right is None:
        # branch is leaf
        ans += branch.num
        ans %= MOD
      else:
        if left:
          left.num = (base_num + left.val) % MOD
          nodes.append(left)
        if right:
          right.num = (base_num + right.val) % MOD
          nodes.append(right)
    return ans





def test():
  s = Solution()
  t1 = make_simple_tree(1,make_simple_tree(0,0,1),make_simple_tree(1,0,1))
  assert s.sumRootToLeaf(t1) == 22

  assert s.sumRootToLeaf(make_simple_tree(1,None,None)) == 1
  assert s.sumRootToLeaf(make_simple_tree(0,None,None)) == 0
