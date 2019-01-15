# coding: utf-8

__author__ = '代码会说话'
"""
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
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
    def buildTree(self, preorder:List[int], inorder:List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        mid = preorder[0]
        mid_index = inorder.index(mid)
        left_inorder = inorder[0:mid_index]
        right_inorder = inorder[mid_index+1:]
        left_pre_end_index = 1 + len(left_inorder)
        left_preorder = preorder[1:left_pre_end_index]
        right_preorder = preorder[left_pre_end_index:]

        root = TreeNode(mid)
        if left_inorder:
            root.left = self.buildTree(left_preorder,left_inorder)
        if right_inorder:
            root.right = self.buildTree(right_preorder,right_inorder)
        return root


"""
  1
 /
2
 \
  3
  
   4
  /
  2
 / \
1   3

"""

def test():
    s = Solution()
    t3 = s.buildTree([4,2,1,3],[1,2,3,4])
    assert levelVisit(t3) == [4,2,1,3]
    t2 = s.buildTree([1,2,3],[1,2,3])
    assert levelVisit(t2) == [1,2,3]
    t1 = s.buildTree([3,9,20,15,7], [9,3,15,20,7])
    assert levelVisit(t1) == [3,9,20,15,7]
