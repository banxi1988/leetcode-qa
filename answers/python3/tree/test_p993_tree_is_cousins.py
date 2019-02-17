# coding: utf-8

__author__ = '代码会说话'

from tree_node import  *



from collections import  deque
class Solution:
  def isCousins(self, root: 'TreeNode', x: 'int', y: 'int') -> 'bool':
    val_to_parent = {}
    val_to_degree = {}
    val_to_degree[root.val] = 0
    nodes = deque([root])
    while nodes:
      node = nodes.popleft()
      degree = val_to_degree[node.val]
      left = node.left
      right = node.right
      if left:
        val_to_parent[left.val] = node.val
        val_to_degree[left.val] = degree + 1
        nodes.append(left)
      if right:
        val_to_parent[right.val] = node.val
        val_to_degree[right.val] = degree + 1
        nodes.append(right)

    xdegree = val_to_degree[x]
    ydegree = val_to_degree[y]
    if xdegree == ydegree:
      xp = val_to_parent.get(x, 0)
      yp = val_to_parent.get(y, 0)
      if xp and yp and (xp != yp):
        return True
    return False


def test():
  s = Solution()
  t1 = make_simple_tree(1,2,3)
  t1.left.left = TreeNode(4)
  assert s.isCousins(root=t1,x=4,y=3) == False
  t2 = make_simple_tree(1,2,3)
  t2.left.right = TreeNode(4)
  t2.right.right = TreeNode(5)
  assert s.isCousins(root=t2,x=5,y=4)

  codec = Codec()
  t3 = codec.deserialize("[1,2,3,null,null,4,5]")
  assert s.isCousins(root=t3,x=4,y=5) == False

  t4 = codec.deserialize("[1,2,4,3,19,10,5,15,8,null,null,13,14,null,6,null,17,null,null,null,null,18,null,7,11,null,null,null,null,null,9,16,12,null,null,20]")
  assert s.isCousins(root=t4, x = 11, y = 17) == False
