# coding: utf-8

__author__ = '代码会说话'

"""
给你一个由若干 0 和 1 组成的二维网格 grid，请你找出边界全部由 1 组成的最大 正方形 子网格，并返回该子网格中的元素数量。如果不存在，则返回 0。

 

示例 1：

输入：grid = [[1,1,1],[1,0,1],[1,1,1]]
输出：9
示例 2：

输入：grid = [[1,1,0,0]]
输出：1
 

提示：

1 <= grid.length <= 100
1 <= grid[0].length <= 100
grid[i][j] 为 0 或 1
"""

from typing import List
from functools import lru_cache
from collections import defaultdict, Counter


class Solution:
  def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
    R = len(grid)
    C = len(grid[0])
    max_side = min(R,C)
    def is_valid_grid(sr,sc,side):
      dc = sc + side -1
      dr = sr + side -1
      for r in range(sr,sr + side):
        if grid[r][sc] != 1 or grid[r][dc] != 1:
          return False
      for c in range(sc,sc + side):
        if grid[sr][c] != 1 or grid[dr][c] != 1:
          return False
      return True


    while max_side > 0:
      for sr in range(0,R - max_side + 1):
        for sc in range(0, C - max_side + 1):
          if is_valid_grid(sr,sc,max_side):
            return max_side * max_side
      max_side -= 1
    return 0



def test():
  s = Solution()
  assert s.largest1BorderedSquare(grid = [[1,1,0,0]]) == 1
  assert s.largest1BorderedSquare(grid = [[1,1,1],[1,0,1],[1,1,1]]) == 9
  assert s.largest1BorderedSquare(grid=[[1,0,0,0,1],[0,1,1,1,1],[1,0,1,1,1],[1,0,1,0,1],[1,1,1,1,1]]) == 9
  assert s.largest1BorderedSquare(grid=[[1,0,0,0,1],[1,1,1,1,1],[1,0,1,1,1],[1,0,1,0,1],[1,1,1,1,1]]) == 9
