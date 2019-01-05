# coding: utf-8

__author__ = '代码会说话'
"""

给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]
      6
    /    \
   2       8
  /  \     / \
  0   4   7   9
     / \
    3   5
   
示例 1:

输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
输出: 6 
解释: 节点 2 和节点 8 的最近公共祖先是 6。
示例 2:

输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
输出: 2
解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。
 

说明:

所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉搜索树中。

  3
1  4
 2
"""

from tree_node import  *

class Solution:
  def lowestCommonAncestor(self, root:TreeNode, p:TreeNode, q:TreeNode) -> TreeNode:
    min_val = min(p.val, q.val)
    max_val = max(p.val, q.val)
    nodes = [root]
    while nodes:
      node = nodes.pop(0)
      val = node.val
      if val == min_val or val == max_val:
        return node
      if val > min_val and val < max_val:
        return node
      left = node.left
      right = node.right
      if val > min_val and left:
        nodes.append(left)
      if val < max_val and right:
        nodes.append(right)





def test():
  s = Solution()
  t2 = make_simple_tree(3,1,4)
  t2.left.right = TreeNode(2)
  assert s.lowestCommonAncestor(t2,TreeNode(2), TreeNode(4)).val == 3
  assert s.lowestCommonAncestor(t2,TreeNode(2), TreeNode(3)).val == 3
  t1 = make_simple_tree(6,
                        make_simple_tree(2,0, make_simple_tree(4,3,5)),
                        make_simple_tree(8,7,9)
                        )
  assert [6,2,8,0,4,7,9,3,5] == levelVisit(t1)

  assert s.lowestCommonAncestor(t1,TreeNode(2), TreeNode(8)).val == 6
  assert s.lowestCommonAncestor(t1,TreeNode(2), TreeNode(4)).val == 2


