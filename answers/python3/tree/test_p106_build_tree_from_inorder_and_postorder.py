# coding: utf-8

__author__ = '代码会说话'
"""
根据一棵树的中序遍历与后序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

中序遍历 inorder = [9,3,15,20,7]
后序遍历 postorder = [9,15,7,20,3]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
"""

from tree_node import  *

from typing import List,Optional

class Solution:
  def buildTree(self, inorder:List[int], postorder:List[int]) -> Optional[TreeNode]:
    if not inorder:
      return None
    if len(inorder) == 1:
      return TreeNode(inorder[0])
    mid = postorder[-1]
    mid_index = inorder.index(mid)
    left_inorder = inorder[0:mid_index]
    right_inorder = inorder[mid_index+1:]
    left_post_end_index = len(left_inorder)
    left_postorder = postorder[:left_post_end_index]
    right_postorder = postorder[left_post_end_index:len(postorder) -1]

    root = TreeNode(mid)
    if left_inorder:
      root.left = self.buildTree(left_inorder,left_postorder)
    if right_inorder:
      root.right = self.buildTree(right_inorder,right_postorder)
    return root


"""
  1
 /
2
 \
  3
"""

def test():
  s = Solution()
  t3 = s.buildTree([1,2,3,4],[1,3,2,4])
  assert levelVisit(t3) == [4,2,1,3]
  t2 = s.buildTree([2,3,1],[3,2,1])
  assert levelVisit(t2) == [1,2,3]
  t1 = s.buildTree([9,3,15,20,7], [9,15,7,20,3])
  assert levelVisit(t1) == [3,9,20,15,7]



