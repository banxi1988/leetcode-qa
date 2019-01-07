# coding: utf-8

__author__ = '代码会说话'
"""
数据结构二叉树(3) 二叉树的中序遍历的递归算法与迭代算法 by 代码会说话

"""
from typing import Callable, Any, Generator, Union, List


class TreeNode:
  def __init__(self, x:int):
    self.val = x
    self.left = None # type: TreeNode
    self.right = None # type: TreeNode

  def __repr__(self):
    return self.__str__()

  def __str__(self):
    return str(self.val)

  def __iter__(self):
    return bt_levelorder_generator(self)

  def find_child_node_by_val(self,val:int):
    for node in self:
      if node.val == val:
        return node


class TreeNodeIterator:
  def __init__(self, tree: TreeNode):
    self._nodes = [tree]

  def __next__(self):
    try:
      node = self._nodes.pop(0)
    except IndexError:
      raise StopIteration
    else:
      left = node.left
      right = node.right
      if left:
        self._nodes.append(left)
      if right:
        self._nodes.append(right)
    return node

  def __iter__(self):
    return self

def bt_levelorder_generator(tree:TreeNode):
  nodes = [tree]
  while nodes:
    node = nodes.pop(0)
    yield node
    if node.left:
      nodes.append(node.left)
    if node.right:
      nodes.append(node.right)




def make_simple_tree(rootVal:int,left:Union[int,TreeNode,None], right:Union[int,TreeNode,None]) -> TreeNode:
  """
    1
  /  \
  2   3
  """
  root = TreeNode(rootVal)
  if isinstance(left,int):
    root.left = TreeNode(left)
  else:
    root.left = left
  if isinstance(right, int):
    root.right = TreeNode(right)
  else:
    root.right = right
  return root

def make_basic_tree():
  """
    1
   / \
  2    3
/ \   /  \
4  5  6   7
  """
  root = TreeNode(1)
  root.left = make_simple_tree(2,4,5)
  root.right = make_simple_tree(3,6,7)
  return root

def bt_preorder_generator(root:TreeNode):
  visited = []
  nodes = [root]
  while nodes:
    node = nodes.pop()
    yield  node
    visited.append(node)
    left = node.left
    if left:
      nodes.append(left)

    while not nodes:
      if visited:
        vnode = visited.pop()
        if vnode.right:
          nodes.append(vnode.right)
      else:
        break


def bt_inorder_generator(root:TreeNode):
  # 1,2,4
  nodes = []
  def collect_left_most(branch:TreeNode):
    p = branch
    while p:
      nodes.append(p)
      p = p.left
  collect_left_most(root)
  while nodes:
    node = nodes.pop()
    yield node
    if node.right:
      collect_left_most(node.right)



def bst_generator(root:TreeNode):
  return bt_inorder_generator(root)

def is_valid_bst(root:TreeNode):
  if not root:
    return True
  import sys
  prev = -sys.maxsize -1
  for node in bst_generator(root):
    val = node.val
    if val <= prev:
      return False
    prev = val
  return  True



def inorder_traversal(root: TreeNode):
  def inorder(branch: TreeNode, out: List[int]):
    if branch.left:
      inorder(branch.left, out)
    out.append(branch.val)
    if branch.right:
      inorder(branch.right, out)
  out = []
  inorder(root, out)
  return out



def test_inorder_traversal():
  t1 = make_basic_tree()
  assert [4, 2,5, 1,6, 3 ,7] == inorder_traversal(t1)

  nums = [node.val for node in bt_inorder_generator(t1)]
  assert [4, 2,5, 1,6, 3 ,7] == nums

def preorder_traversal(root: TreeNode):
  def preorder(branch: TreeNode, out: List[int]):
    out.append(branch.val)
    if branch.left:
      preorder(branch.left, out)
    if branch.right:
      preorder(branch.right, out)
  out = []
  preorder(root, out)
  return out

def test_preorder_traversal():
  """
   2
3   1
 \
  5
   \
    4
  :return:
  """
  t2 = make_simple_tree(2,3,1)
  t2.left.right = make_simple_tree(5,None,4)
  nums2 = [node.val for node in bt_preorder_generator(t2)]
  assert [2,3,5,4,1] == nums2

  t1 = make_basic_tree()
  assert [1,2,4,5,3,6,7] == preorder_traversal(t1)
  nums = [node.val for node in bt_preorder_generator(t1)]
  assert [1,2,4,5,3,6,7] == nums

def postorder_traversal(root: TreeNode):
  def postorder(branch: TreeNode, out: List[int]):
    if branch.left:
      postorder(branch.left, out)
    if branch.right:
      postorder(branch.right, out)
    out.append(branch.val)
  out = []
  postorder(root, out)
  return out

def bt_postorder(root:TreeNode):
  nodes = [root]
  passed = []
  while nodes:
    node = nodes.pop()
    passed.insert(0,node)
    right = node.right
    left = node.left
    if left:
      nodes.append(left)
    if right:
      nodes.append(right)

  nums = [node.val for node in passed]
  return nums

def test_postorder_traversal():
  """
   2
3   1
 \
  5
   \
    4
  :return:
  """
  t2 = make_simple_tree(2,3,1)
  t2.left.right = make_simple_tree(5,None,4)
  assert [4,5,3,1,2] == bt_postorder(t2)

  t1 = make_basic_tree()
  n4 = t1.find_child_node_by_val(4)
  n4.right = make_simple_tree(8,9, None)
  assert [9,8,4,5,2,6,7,3,1] == postorder_traversal(t1)
  assert [9,8,4,5,2,6,7,3,1] == bt_postorder(t1)

def levelTraversal(tree:TreeNode,visitFn:Callable[[TreeNode],Any]):
  if tree is None:
    return
  nodes = [tree]
  while nodes:
    node = nodes.pop(0)
    visitFn(node)
    left = node.left
    right = node.right
    if left:
      nodes.append(left)
    if right:
      nodes.append(right)

def levelOrder(root:TreeNode) -> List[List[int]]:
    if not root:
      return []
    nodes = [root]
    root.level = 1
    result = []
    level_list = []
    prev_level = 0
    while nodes:
      node = nodes.pop(0)
      level = node.level
      if level > prev_level:
        if level_list:
          result.append(level_list)
        level_list = []
        prev_level = level
      level_list.append(node.val)
      left = node.left
      right = node.right

      if left:
        left.level = level + 1
        nodes.append(left)
      if right:
        right.level = level + 1
        nodes.append(right)

    if level_list:
      result.append(level_list)

    return result

def levelVisit(tree:TreeNode):
  if tree is None:
    return []
  values = []
  levelTraversal(tree,lambda node: values.append(node.val))
  return values


def test_levelVisit():
  t1 = make_basic_tree()
  assert [1,2,3,4,5,6,7] ==  levelVisit(t1)

def test_iter_levelVisit():
  root = make_basic_tree()
  l1 = [node.val for node in root]
  assert [1,2,3,4,5,6,7] == l1


def depthOfTree_r(tree:TreeNode)->int:
  if tree is None:
    return 0

  left_depth = depthOfTree_r(tree.left)
  right_depth = depthOfTree_r(tree.right)
  return 1 + max(left_depth, right_depth)

def test_depthOfTree_r():
  t1 = make_simple_tree(1,2,3)
  assert depthOfTree_r(t1) == 2
  t2 = make_basic_tree()
  assert depthOfTree_r(t2) == 3
  t3 = TreeNode(1)
  assert depthOfTree_r(t3) == 1

def depthOfTree(tree:TreeNode):
  if tree is None:
    return 0
  nodes = [tree]
  max_depth = 1
  node_to_depth = {tree: 1}
  while nodes:
    node = nodes.pop(0)
    depth = node_to_depth[node]
    left = node.left
    right = node.right
    depth += 1
    if left:
      max_depth = max(max_depth, depth)
      node_to_depth[left] = depth
      nodes.append(left)
    if right:
      max_depth = max(max_depth, depth)
      node_to_depth[right] = depth
      nodes.append(right)
  return max_depth

def test_depthOfTree():
  t1 = make_simple_tree(1,2,3)
  assert depthOfTree(t1) == 2
  t2 = make_basic_tree()
  assert depthOfTree(t2) == 3

  t3 = TreeNode(1)
  assert depthOfTree(t3) == 1