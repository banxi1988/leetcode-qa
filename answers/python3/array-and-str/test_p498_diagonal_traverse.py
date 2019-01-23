# coding: utf-8

__author__ = '代码会说话'

"""
给定一个含有 M x N 个元素的矩阵（M 行，N 列），请以对角线遍历的顺序返回这个矩阵中的所有元素，对角线遍历如下图所示。

 

示例:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

输出:  [1,2,4,7,5,3,6,8,9]

解释:

 

说明:

给定矩阵中的元素总数不会超过 100000 。
"""

from typing import List
from collections import deque

class Solution:
  def findDiagonalOrder(self, matrix:List[List[int]]) ->List[int]:
    if not matrix:
      return []
    row_count = len(matrix)
    col_count = len(matrix[0])
    nums = deque()
    append = False
    for start_col in range(col_count + row_count -1):
      col = min(start_col,col_count -1)
      row = 0 if start_col < col_count else (start_col - col_count + 1)
      round_nums = deque()
      while row < row_count and col > -1:
        num = matrix[row][col]
        if append:
          round_nums.append(num)
        else:
          round_nums.appendleft(num)
        row += 1
        col -= 1
      append = not append
      nums.extend(round_nums)
    return list(nums)



def test():
  s = Solution()
  assert s.findDiagonalOrder([
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
  ]) == [1,2,4,7,5,3,6,8,9]

  assert s.findDiagonalOrder([
    [ 1, 2, 3 ],
    [ 7, 8, 9 ]
  ]) == [1,2,7,8,3,9]
