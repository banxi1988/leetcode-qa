# coding: utf-8

__author__ = '代码会说话'



from typing import List

class Orange:
  def __init__(self,row:int,col:int,fresh:int):
    self.row = row
    self.col = col
    self.fresh = fresh

  def __str__(self):
    return "(%d,%d)=%d" % (self.row,self.col,self.fresh)

  def __repr__(self):
    return str(self)

class Solution:
  def orangesRotting(self, grid: 'List[List[int]]') -> 'int':
    bad_oranges = []
    fresh_count = 0
    bad_count = 0
    pos_to_orange = {}
    for r,row in enumerate(grid):
      for c,fresh in enumerate(row):
        if fresh > 0:
          orange = Orange(row=r,col=c,fresh=fresh)
          pos_to_orange[(r,c)] = orange
          if fresh == 1:
            fresh_count += 1
          elif fresh == 2:
            bad_count += 1
            bad_oranges.append(orange)

    if fresh_count < 1:
      return  0
    if bad_count < 1:
      return  -1
    #total_count = bad_count + fresh_count
    minutes = 0
    while len(bad_oranges):
      next_bad_oranges = []
      round_changed = 0
      for bad in bad_oranges:
        r = bad.row
        c = bad.col
        changed = 0
        for pos in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
          orange = pos_to_orange.get(pos)
          if orange and orange.fresh == 1:
            orange.fresh = 2
            changed += 1
            next_bad_oranges.append(orange)
            fresh_count -= 1
            bad_count += 1
        round_changed += changed

      bad_oranges = next_bad_oranges
      if round_changed:
        minutes += 1
    if fresh_count == 0:
      return minutes
    return -1







def test():
  s = Solution()
  assert s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]) == 4
  assert s.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]) == -1
  assert s.orangesRotting([[0,2]]) == 0
  assert s.orangesRotting([[0]]) == 0
