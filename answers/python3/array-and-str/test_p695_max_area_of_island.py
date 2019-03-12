# coding: utf-8

__author__ = '代码会说话'

"""
LeetCode 695. 岛屿的最大面积

给定一个包含了一些 0 和 1的非空二维数组 grid , 一个 岛屿 是由四个方向 (水平或垂直) 的 1 (代表土地) 构成的组合。
你可以假设二维矩阵的四个边缘都被水包围着。

找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为0。)

示例 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
 
对于上面这个给定矩阵应返回 6。注意答案不应该是11，因为岛屿只能包含水平或垂直的四个方向的‘1’。

示例 2:

[[0,0,0,0,0,0,0,0]]
对于上面这个给定的矩阵, 返回 0。

注意: 给定的矩阵grid 的长度和宽度都不超过 50。
50x50
"""

from typing import List


class Solution:
  VISITED = -1  # !=1
  ISLAND = 1

  def maxAreaFrom(self, grid: List[List[int]], r: int, c: int) -> int:
    R = len(grid)
    C = len(grid[0])
    area = 1
    grid[r][c] = self.VISITED
    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
      nr = r + dr
      nc = c + dc
      if nr > -1 and nr < R and nc > -1 and nc < C:
        if grid[nr][nc] == self.ISLAND:
          area += self.maxAreaFrom(grid, nr, nc)
    return area

  def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    max_area = 0
    R = len(grid)
    C = len(grid[0])
    for r in range(R):
      for c in range(C):
        val = grid[r][c]
        if val != self.ISLAND:
          continue
        area = self.maxAreaFrom(grid, r, c)
        max_area = max(area, max_area)

    return max_area


def test():
  s = Solution()
  assert s.maxAreaOfIsland([[0, 0, 0, 0, 0, 0, 0, 0]]) == 0
  assert s.maxAreaOfIsland([[1, 1, 0, 0, 0],
                            [1, 1, 0, 0, 0],
                            [0, 0, 0, 1, 1],
                            [0, 0, 0, 1, 1]]) == 4

  assert s.maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]) == 6
