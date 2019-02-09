# coding: utf-8

__author__ = '代码会说话'

"""
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]
"""

from typing import List
class Solution:
  def prisonAfterNDays(self, cells:List[int], N:int) -> List[int]:
    cell_count = len(cells)
    prev_cells = cells
    for _ in range(0,N):
      new_cells = [0] * cell_count
      for i in range(1,cell_count-1):
        new_cells[i] = 1 if  prev_cells[i-1] == prev_cells[i + 1]  else 0
      prev_cells = new_cells

    return prev_cells



def test():
  s = Solution()
  assert s.prisonAfterNDays([0,1,0,1,1,0,0,1],7) == [0,0,1,1,0,0,0,0]

  assert s.prisonAfterNDays([1,0,0,1,0,0,1,0],1000000000) == [0,0,1,1,1,1,1,0]

