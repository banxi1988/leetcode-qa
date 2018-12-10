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

from typing import  List,Union
class Solution:
  def maximalSquare(self, matrix: List[List[Union[int,str]]]) -> int:
    rows = len(matrix)
    if not rows:
      return 0
    cols = len(matrix[0])
    if not cols:
      return  0
    max_size = 0

    def isSquare(row:int,col:int,size:int) -> bool:
      #print("(%d,%d,%d)" % (row,col,size))
      if  (row + size) > rows or (col + size) > cols:
        return False
      for i in range(0,size):
        for j in range(0,size):
          val = matrix[row + i][col + j]
          if val != 1 and val != '1':
            return False
      return True

    for row in range(0, rows):
      for col in range(0,cols):
        origin = matrix[row][col]
        if origin!= 1 and origin != '1':
          continue
        size = max_size + 1
        is_square = isSquare(row,col, size)
        while is_square:
          max_size = size
          size += 1
          is_square = isSquare(row,col, size)
    return max_size * max_size



def test():
  s = Solution()
  assert s.maximalSquare([]) == 0
  assert s.maximalSquare([[]]) == 0
  m12 = [
    [1,0,1,0,0,0,0],
    [1,0,1,1,1,1,1],
    [1,1,1,1,1,1,1],
    [1,0,0,1,1,1,0],
  ]
  assert s.maximalSquare(m12) == 9
  return
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
