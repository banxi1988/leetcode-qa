# coding: utf-8

__author__ = '代码会说话'

"""
p58 螺旋矩阵
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
示例 2:

输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]

R:3 -> 0,1,2
C:4 -> 0,1,2,3

r:0,0,0,0,1,2,2,2,2,1,1  2,2
c:0,1,2,3,3,3,2,1,0,1,2
"""

from typing import List

from enum import IntEnum

class Direction(IntEnum):
  FORWARD = 0
  DOWN = 1
  BACKRWARD = 2
  UP = 3


class Solution:
  def spiralOrder(self, matrix:List[List[int]]) -> List[int]:
    if not matrix:
      return []
    min_row = 0
    max_row = len(matrix) -1
    min_col = 0
    max_col = len(matrix[0]) -1
    direction = Direction.FORWARD
    nums = []
    row = 0
    col = 0
    while True:
      nums.append( matrix[row][col])

      if direction == Direction.FORWARD:
        col += 1
      elif direction == Direction.BACKRWARD:
        col -= 1
      elif direction == Direction.DOWN:
        row += 1
      else:
        row -=1
      if row < min_row or row > max_row or col < min_col or col > max_col:
        if direction == Direction.FORWARD:
          min_row += 1
        elif direction == Direction.BACKRWARD:
          max_row -= 1
        elif direction == Direction.DOWN:
          max_col -= 1
        else:
          min_col +=1
        if min_col > max_col or min_row > max_row:
          break
        row = max(min(max_row, row),min_row)
        col = max(min(max_col, col),min_col)
        next_direction = (direction + 1) % 4
        direction = next_direction
    return nums








def test():
  s = Solution()

  assert s.spiralOrder([
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
  ]) == [1,2,3,6,9,8,7,4,5]

  assert s.spiralOrder([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9,10,11,12]
  ]) == [1,2,3,4,8,12,11,10,9,5,6,7]
