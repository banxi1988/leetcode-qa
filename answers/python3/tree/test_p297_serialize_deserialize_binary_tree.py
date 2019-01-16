# coding: utf-8

__author__ = '代码会说话'

"""
序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

示例: 

你可以将以下二叉树：

    1
   / \
  2   3
     / \
    4   5

序列化为 "[1,2,3,null,null,4,5]"
提示: 这与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。

说明: 不要使用类的成员 / 全局 / 静态变量来存储状态，你的序列化和反序列化算法应该是无状态的。
"""

from tree_node import *


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






  def deserialize(self, data:str) -> TreeNode:
    if  len(data) < 3:
      return None
    list_str = data[1:len(data) -1]


def test():
  s = Codec()
  t1 = make_simple_tree(1,2,make_simple_tree(3,4,5))
  assert s.serialize(t1) == "[1,2,3,null,null,4,5]"
  assert s.serialize(None) == '[]'
  assert s.serialize(make_simple_tree(1,2,3)) == '[1,2,3]'

  t3 = make_simple_tree(1,None,make_simple_tree(2,3,None))
  assert s.serialize(t3) == '[1,null,2,3]'
  t4 = make_flat_tree([5,4,3,-1])
  t4.right = make_flat_tree([7,2,9])
  assert s.serialize(t4) == '[5,4,7,3,null,2,null,-1,null,9]'

