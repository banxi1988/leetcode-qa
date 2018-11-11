# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        branches = [root]
        sum = 0
        while len(branches) > 0:
            node = branches[0]
            branches = branches[1:]
            val = node.val
            if val >= L and val <= R:
                sum += val
            if node.right:
                if val < R:
                    branches.append(node.right)
            if node.left:
                if val > L:
                    branches.append(node.left)

        return sum


def test_wc110_p2():
    tree1 = TreeNode(10)
    tree1.left = TreeNode(5)
    tree1.right = TreeNode(15)
    tree1.left.left = TreeNode(3)
    tree1.left.right = TreeNode(7)
    tree1.right.right = TreeNode(18)

    solution = Solution()
    assert solution.rangeSumBST(tree1, 7, 15) == 32

    tree2 = TreeNode(10)
    tree2.left = TreeNode(5)
    tree2.right = TreeNode(15)
    tree2.left.left = TreeNode(3)
    tree2.left.left.left = TreeNode(1)
    tree2.left.right = TreeNode(7)
    tree2.left.right.left = TreeNode(6)
    tree2.right.left = TreeNode(13)
    tree2.right.right = TreeNode(18)

    assert solution.rangeSumBST(tree2, 6, 10) == 23
    # assert solution.rangeSumBST(tree2, 3, 7) == 15

    tree3 = TreeNode(18)
    tree3.left = TreeNode(9)
    tree3.right = TreeNode(27)
    tree3.left.left = TreeNode(6)
    tree3.left.right = TreeNode(15)
    tree3.left.left.left = TreeNode(3)
    tree3.left.right.left = TreeNode(12)

    tree3.right.left = TreeNode(24)
    tree3.right.left.left = TreeNode(21)
    tree3.right.right = TreeNode(30)

    assert solution.rangeSumBST(tree3, 18, 24) == 63
