# coding: utf-8

__author__ = '代码会说话'

"""
实现一个二叉搜索树迭代器。你将使用二叉搜索树的根节点初始化迭代器。

调用 next() 将返回二叉搜索树中的下一个最小的数。


示例：
  7
 / \
3   15
   /  \
  9   20


BSTIterator iterator = new BSTIterator(root);
iterator.next();    // 返回 3
iterator.next();    // 返回 7
iterator.hasNext(); // 返回 true
iterator.next();    // 返回 9
iterator.hasNext(); // 返回 true
iterator.next();    // 返回 15
iterator.hasNext(); // 返回 true
iterator.next();    // 返回 20
iterator.hasNext(); // 返回 false
 

提示：

next() 和 hasNext() 操作的时间复杂度是 O(1)，并使用 O(h) 内存，其中 h 是树的高度。
你可以假设 next() 调用总是有效的，也就是说，当调用 next() 时，BST 中至少存在一个下一个最小的数。
"""

from tree_node import *

class BSTIterator:
  def __init__(self, root:TreeNode):
    self.left_most = []
    self.collect_left_most(root)

  def collect_left_most(self, node:TreeNode):
    p = node
    while p:
      self.left_most.append(p)
      p = p.left


  def next(self) -> int:
    min = self.left_most.pop()
    if min.right:
      self.collect_left_most(min.right)
    return min.val

  def hasNext(self) -> bool:
    return len(self.left_most) > 0


def test():
  t1 = make_simple_tree(7, 3, make_simple_tree(15,9,20))
  it = BSTIterator(t1)
  assert it.next() == 3
  assert it.next() == 7
  assert it.next() == 9
  assert it.next() == 15
  assert it.next() == 20
  assert it.hasNext() == False

