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

输出: 4
"""

from typing import  List
class Solution:
  def maximalSquare(self, matrix: List[List[int]]) -> int:
    rows = len(matrix)
    cols = len(matrix[0])
    max_area = 0

    def isSquare(row:int,col:int,size:int) -> bool:
      if  (row + size) > rows or (col + size) > cols:
        return False
      for i in range(0,size):
        for j in range(0,size):
          if matrix[row + i][col + j] != 1:
            return False
      return True

    for row in range(0, rows):
      for col in range(0,cols):
        if matrix[row][col] != 1:
          continue
        size = 1
        is_square = True
        while is_square:
          area = size * size
          if area > max_area:
            max_area = area
          size += 1
          is_square = isSquare(row,col, size)
    return max_area



def test():
  s = Solution()
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
