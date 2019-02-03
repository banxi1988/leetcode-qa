# coding: utf-8

__author__ = '代码会说话'
"""
988. 从叶结点开始的最小字符串

给定一颗根结点为 root 的二叉树，书中的每个结点都有一个从 0 到 25 的值，分别代表字母 'a' 到 'z'：值 0 代表 'a'，值 1 代表 'b'，依此类推。

找出按字典序最小的字符串，该字符串从这棵树的一个叶结点开始，到根结点结束。

（小贴士：字符串中任何较短的前缀在字典序上都是较小的：例如，在字典序上 "ab" 比 "aba" 要小。叶结点是指没有子结点的结点。）

 

示例 1：



输入：[0,1,2,3,4,3,4]
输出："dba"
示例 2：



输入：[25,1,3,1,3,0,2]
输出："adz"
示例 3：



输入：[2,2,1,null,1,0,null,0]
输出："abc"
 

提示：

给定树的结点数介于 1 和 1000 之间。
树中的每个结点都有一个介于 0 和 25 之间的值。

"""

from tree_node import *


class Solution:
  def smallestFromLeaf(self, root: 'TreeNode') -> 'str':
    left = root.left
    right = root.right
    ch = chr(ord('a') + root.val)
    if left and right:
      r1 = self.smallestFromLeaf(left)
      r2 = self.smallestFromLeaf(right)
      return r1 + ch if r1 < r2 else r2 + ch
    elif left or right:
      child = left if left else right
      r1 = self.smallestFromLeaf(child)
      return r1 + ch
    else:
      return ch



def test():
  codec = Codec()
  t1 = codec.deserialize("[0,1,2,3,4,3,4]")
  s = Solution()
  assert s.smallestFromLeaf(t1) == "dba"

  t2 = codec.deserialize("[25,1,3,1,3,0,2]")
  assert s.smallestFromLeaf(t2) == "adz"

  t3 = codec.deserialize("[2,2,1,null,1,0,null,0]")
  assert s.smallestFromLeaf(t3) == "abc"
