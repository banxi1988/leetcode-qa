# coding: utf-8

__author__ = '代码会说话'
"""
数据结构二叉树(4) 二叉树的前序遍历的递归算法与迭代算法 by 代码会说话

"""
from typing import Callable, Any, Generator, Union, List, Optional
from collections import deque


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

  def __eq__(self, other):
    if not isinstance(other,TreeNode):
      return False
    return is_same_tree(self,other)


class TreeNodeIterator:
  def __init__(self, tree: TreeNode):
    self._nodes = deque()
    self._nodes.append(tree)

  def __next__(self):
    try:
      node = self._nodes.popleft()
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

def is_same_tree(t1:Union[TreeNode,None],t2:Union[TreeNode,None])->bool:
  if t1 and t2:
    if t1.val != t2.val:
      return False
    return is_same_tree(t1.left,t2.left) and is_same_tree(t1.right, t2.right)
  elif t1 or t2:
    return False
  else:
    return True

def test_is_same_tree():
  t1 = make_simple_tree(1,2,3)
  t1_2 = make_simple_tree(1,2,3)
  t2 = make_simple_tree(1,3,2)
  t3 = make_simple_tree(1,3,None)
  assert is_same_tree(t1,t1_2)
  assert t1 == t1_2
  assert is_same_tree(t1,t2) == False
  assert t1 != t2
  assert is_same_tree(t1,t3) == False
  assert t1 != t3

def is_balanced_tree(tree:TreeNode) -> bool:
  if not tree:
    return True
  level_nodes = [tree]
  node_count = 0
  max_degree = 0
  level_nodes_list =[]

  while level_nodes:
    level_nodes_list.append(level_nodes)
    next_level_nodes =[]
    for node in level_nodes:
      node_count += 1
      left = node.left
      right = node.right
      node.degree = 0
      if left:
        left.parent = node
        next_level_nodes.append(left)
      if right:
        right.parent = node
        next_level_nodes.append(right)
    if next_level_nodes:
      max_degree += 1
    level_nodes = next_level_nodes
  for node in level_nodes_list[-1]:
    node.degree = 0
  for level_nodes in reversed(level_nodes_list):
    for node in level_nodes:
      if hasattr(node,'parent'):
        parent = node.parent
        parent.degree = max(node.degree +1,parent.degree)
  for level_nodes in level_nodes_list:
    for node in level_nodes:
      left_degree = node.left.degree if node.left else -1
      right_degree = node.right.degree if node.right else -1
      if abs(left_degree - right_degree) > 1:
        return False
  return True


def test_is_balanced_tree():
  codec = Codec()
  t4 = codec.deserialize("[1,null,2,null,3]")
  assert not is_balanced_tree(t4)
  t2 = codec.deserialize("[1,2,2,3,3,null,null,4,4]")
  assert not is_balanced_tree(t2)
  t1 = codec.deserialize("[1,2,2,3,3,3,3,4,4,4,4,4,4,null,null,5,5]")
  assert is_balanced_tree(t1)

  t3 = codec.deserialize("[3,9,20,null,null,15,7]")
  assert is_balanced_tree(t3)




def bt_levelorder_generator(tree:TreeNode):
  nodes = deque()
  nodes.append(tree)
  while nodes:
    node = nodes.popleft()
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

def make_flat_tree(nums:List[int],left_leaning=True):
  dummy = TreeNode(0)
  p = dummy
  for num in nums:
    if left_leaning:
      p.left = TreeNode(num)
      p = p.left
    else:
      p.right = TreeNode(num)
      p = p.right

  return dummy.left if left_leaning else dummy.right


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
  out = []
  def preorder(branch:TreeNode):
    out.append(branch.val)
    if branch.left:
      preorder(branch.left)
    if branch.right:
      preorder(branch.right)

  preorder(root)
  return  out

def bt_preorder_generator(root:TreeNode):
  """
    1
   / \
  2    3
/ \   /  \
4  5  6   7

  """
  visited = []
  nodes = [root]
  while nodes:
    node = nodes.pop()
    yield node
    visited.append(node)
    if node.left:
      nodes.append(node.left)

    while not nodes:
      if visited:
        vnode = visited.pop()
        if vnode.right:
          nodes.append(vnode.right)
      else:
        break




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

def preorder_symmetric_traversal(root: TreeNode):
  out = []
  def preorder(branch:TreeNode):
    out.append(branch.val)
    if branch.right:
      preorder(branch.right)
    if branch.left:
      preorder(branch.left)

  preorder(root)
  return  out

def bt_symmetric_inorder_generator(root:TreeNode):
  """
    1
   / \
  2    3
/ \   /  \
4  5  6   7
  """
  nodes = []
  def collect_right_most(branch:TreeNode):
    right = branch
    while right:
      nodes.append(right)
      right = right.right
  collect_right_most(root)
  while nodes:
    node =  nodes.pop()
    yield node
    if node.left:
      collect_right_most(node.left)

def bt_symmetric_preorder_generator(root:TreeNode):
  """
    1
   / \
  2    3
/ \   /  \
4  5  6   7
N: 1/,3/,7/,6/,2/,5/,4
V:
  """
  nodes = deque([root])
  visited = []
  while nodes:
    node =  nodes.popleft()
    yield node
    if node.left:
      visited.append(node.left)
    if node.right:
      nodes.append(node.right)

    while not nodes:
      if visited:
        node = visited.pop()
        nodes.append(node)
      else:
        break


def test_symmetric_preorder_traversal():
  t1 = make_basic_tree()
  assert [1,3,7,6,2,5,4] == preorder_symmetric_traversal(t1)
  nums = [node.val for node in bt_symmetric_preorder_generator(t1)]
  assert [1,3,7,6,2,5,4] == nums


def postorder_symmetric_traversal(root: TreeNode):
  out = []
  def postorder(branch:TreeNode):
    if branch.right:
      postorder(branch.right)
    if branch.left:
      postorder(branch.left)
    out.append(branch.val)

  postorder(root)
  return  out

def bt_symmetric_postorder(root:TreeNode):
  """
  N:1/,3,2/,5,4/
  V:  5,4,2,1
  """
  nodes = [root]
  visited = deque()
  while nodes:
    node = nodes.pop()
    visited.appendleft(node)
    if node.right:
      nodes.append(node.right)
    if node.left:
      nodes.append(node.left)
  return visited


def test_postorder_symmetric_traversal():
  """
    1
   / \
  2    3
/ \   /  \
4  5  6   7
  """
  t1 = make_basic_tree()
  assert [7,6,3,5,4,2,1] == postorder_symmetric_traversal(t1)
  nums = [node.val for node in bt_symmetric_postorder(t1)]
  assert nums == [7,6,3,5,4,2,1]

"""
数据结构二叉树(5) 二叉树的后序遍历的迭代与递归算法与算法 by 代码会说话

"""

def postorder_traversal(root: TreeNode):
  out = []
  def postorder(branch:TreeNode):
    if branch.left:
      postorder(branch.left)
    if branch.right:
      postorder(branch.right)

    out.append(branch.val)

  postorder(root)
  return out

def bt_postorder(root:TreeNode):
  """

    1
   / \
  2    3
/ \   /  \
4  5  6   7
 \
  8
 /
9

N: 1/,2,3/,6,7
visited:  3, 1
  """
  visited = []
  nodes = [root]
  while nodes:
    node = nodes.pop()
    visited.insert(0, node.val)
    left = node.left
    right = node.right
    if left:
      nodes.append(left)
    if right:
      nodes.append(right)

  return visited



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
  # assert [4,5,3,1,2] == bt_postorder(t2)

  t1 = make_basic_tree()
  n4 = t1.find_child_node_by_val(4)
  n4.right = make_simple_tree(8,9, None)
  assert [9,8,4,5,2,6,7,3,1] == postorder_traversal(t1)
  # assert [9,8,4,5,2,6,7,3,1] == bt_postorder(t1)

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
  nodes = deque()
  nodes.append(tree)
  max_depth = 1
  node_to_depth = {tree: 1}
  while nodes:
    node = nodes.popleft()
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




class Codec:

  def serialize(self, root) -> str:
    if not root:
      return '[]'
    level_nodes = [root]
    sym_nodes = []
    while True:
      next_level_nodes = []
      non_empty_count = 0
      for node in level_nodes:
        sym_nodes.append(node)
        if not node:
          continue
        next_level_nodes.append(node.left)
        next_level_nodes.append(node.right)
        if node.left:
          non_empty_count+= 1
        if node.right:
          non_empty_count+= 1
      if non_empty_count > 0:
        level_nodes = next_level_nodes
      else:
        break
    while sym_nodes[-1] is None:
      sym_nodes.pop()

    symbols = [str(node.val) if node else 'null' for node in sym_nodes]
    return '[' +','.join(symbols) + ']'


  def deserialize(self, data:str):
    from collections import deque
    if  len(data) < 3:
      return None
    list_str = data[1:len(data) -1]
    symbols = deque(s.strip() for s in list_str.split(","))
    root = TreeNode(int(symbols.popleft()))
    prev_level = [root]
    while symbols and prev_level:
      next_level = []
      for parent in prev_level:
        if symbols:
          symbol = symbols.popleft()
          left = TreeNode(int(symbol)) if symbol != 'null' else None
          if left:
            parent.left = left
            next_level.append(left)
        if symbols:
          symbol = symbols.popleft()
          right = TreeNode(int(symbol)) if symbol != 'null' else None
          if right:
            parent.right = right
            next_level.append(right)
      prev_level = next_level

    return root

def bst_insert_r(root:Optional[TreeNode], val:int) -> TreeNode:
  """ 二叉搜索树的递归插入操作 """
  if not root:
    return TreeNode(val)
  if root.val > val:
    root.left = bst_insert_r(root.left, val)
  else:
    root.right = bst_insert_r(root.right, val)
  return root

def bst_insert(root:TreeNode, val:int) -> TreeNode:
  """ 二叉搜索树的递归迭代插入操作 """
  if not root:
    return TreeNode(val)
  prev = root
  while prev:
    if prev.val < val:
      if prev.right:
        prev = prev.right
      else:
        prev.right = TreeNode(val)
        break
    else:
      if prev.left:
        prev = prev.left
      else:
        prev.left = TreeNode(val)
        break
  return root