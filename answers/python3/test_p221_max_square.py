# coding: utf-8

__author__ = '代码会说话'

"""
LeetCode 221. 最大正方形 题解 by 代码会说话

在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

示例:

输入:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

1   1  
2   2 1 1
3 1 3 2 2
4 0 0 0 0

输出: 4
"""

from typing import  List,Union,Optional
class Solution:
  def maximalSquare(self, matrix: List[List[Union[int,str]]]) -> int:
    rows = len(matrix)
    if not rows:
      return 0
    cols = len(matrix[0])
    if not cols:
      return  0
    if rows < 2:
      return max(matrix[0])
    if cols < 2:
      return max(matrix[r][0] for r in range(0,rows))
    max_side = 0
    m = matrix
    for r in range(1, rows):
      for c in range(1, cols):
        cur_max_side = 0
        if m[r][c] == 1:
          cur_max_side = min(m[r][c-1],m[r-1][c],m[r-1][c-1]) + 1
        m[r][c] = cur_max_side
        if cur_max_side > max_side:
          max_side = cur_max_side

    return max_side * max_side



def test():
  s = Solution()
  assert s.maximalSquare([]) == 0
  assert s.maximalSquare([[]]) == 0
  # me1 = [
  #   ["1","0","1","1","0","1"],
  #   ["1","1","1","1","1","1"],
  #   ["0","1","1","0","1","1"],
  #   ["1","1","1","0","1","0"],
  #   ["0","1","1","1","1","1"],
  #   ["1","1","0","1","1","1"]
  # ]
  #
  # assert s.maximalSquare(me1) == 4

  m12 = [
    [1,0,1,0,0,0,0],
    [1,0,1,1,1,1,1],
    [1,1,1,1,1,1,1],
    [1,0,0,1,1,1,0],
  ]
  assert s.maximalSquare(m12) == 9
  # return
  m4 = [
    [1,1,1],
    [1,1,0]
  ]
  assert s.maximalSquare(m4) == 4
  m1 = [
    [1,0,1,0,0],
    [1,0,1,1,1],
    [1,1,1,1,1],
    [1,0,0,1,0],
  ]
  assert s.maximalSquare(m1) == 4


  m11 = [
    [1,0,1,0,0,0,0],
    [1,0,1,1,1,1,1],
    [1,1,1,1,1,1,1],
    [1,0,0,1,0,0,0],
  ]
  assert s.maximalSquare(m11) == 4

  m12 = [
    [1,0,1,0,0,0,0],
    [1,0,1,1,1,1,1],
    [1,1,1,1,1,1,1],
    [1,0,0,1,1,1,0],
  ]
  assert s.maximalSquare(m12) == 9

  m2 = [
    [1]
  ]
  assert s.maximalSquare(m2) == 1
  m3 = [
    [1,1]
  ]
  assert s.maximalSquare(m3) == 1
  m4 = [
    [1,1,1],
    [1,1,0]
  ]
  assert s.maximalSquare(m4) == 4
  m5 = [
    [0,1,1],
    [1,1,1]
  ]
  assert s.maximalSquare(m5) == 4
