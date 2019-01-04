# coding: utf-8

__author__ = '代码会说话'
"""
数据结构二叉树(1) 树的高度及层序遍历  by 代码会说话

"""
from typing import Callable,Any,Generator

class TreeNode:
  def __init__(self, x:int):
    self.val = x
    self.left = None # type: TreeNode
    self.right = None # type: TreeNode

  def __iter__(self):
    # return TreeNodeIterator(self)
    return gen_node(self)

def gen_node(tree:TreeNode) -> Generator[TreeNode,None,None] :
  nodes = [tree]
  while nodes:
    node = nodes.pop(0)
    yield node
    if node.left:
      nodes.append(node.left)
    if node.right:
      nodes.append(node.right)



def make_simple_tree(rootVal:int,left:int, right:int) -> TreeNode:
  """
    1
  /  \
  2   3
  """
  root = TreeNode(rootVal)
  root.left = TreeNode(left)
  root.right = TreeNode(right)
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

class TreeNodeIterator:
  """二叉树的层序遍历迭代器"""
  def __init__(self, tree:TreeNode):
    self._nodes = [tree]

  def __next__(self):
    try:
      node = self._nodes.pop(0)
    except IndexError:
      raise StopIteration()
    else:
      if node.left:
        self._nodes.append(node.left)
      if node.right:
        self._nodes.append(node.right)
      return node
  def __iter__(self):
    return self


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