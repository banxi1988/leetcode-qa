# coding: utf-8

__author__ = '代码会说话'

from tree_node import  *

class MoveStat:
  def __init__(self):
    self.io = 0
    self.steps = 0

  def __str__(self):
    return "%d,%d:%d" % (self.in_count,self.out_count, self.steps)

  def __repr__(self):
    return "MoveStat[%s]" % str(self)

class Solution:
  def distributeCoins(self, root):
    def dist(branch:TreeNode) -> MoveStat:
      if not branch:
        return MoveStat()
      left_stat = dist(branch.left)
      right_stat = dist(branch.right)
      steps =  left_stat.steps + right_stat.steps
      io = left_stat.io + right_stat.io + branch.val - 1
      stat = MoveStat()
      stat.steps = steps + abs(io)
      stat.io = io
      return stat

    stat = dist(root)
    assert stat.io == 0
    return stat.steps



def test():
  s = Solution()

  t2 = make_simple_tree(0,3,0)
  assert s.distributeCoins(t2) == 3

  t1 = make_simple_tree(3,0,0)
  assert s.distributeCoins(t1) == 2

  t3 = make_simple_tree(1,0,2)
  assert s.distributeCoins(t3) == 2

  t4 = make_simple_tree(1,make_simple_tree(0,None,3),0)
  assert s.distributeCoins(t4) == 4