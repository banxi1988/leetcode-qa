# coding: utf-8

__author__ = '代码会说话'

"""
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。



在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

from typing import List

class Solution:
  def generate(self, numRows:int) -> List[List[int]]:
    if numRows == 0:
      return []
    rows = [[1]]
    for count in range(2,numRows + 1):
      prev_row = rows[-1]
      row = [1]
      for c in range(0,count -2):
        num = prev_row[c] + prev_row[c + 1]
        row.append(num)
      row.append(1)
      rows.append(row)

    return rows




def test():
  s = Solution()
  assert s.generate(0) == []
  assert s.generate(1) == [[1]]
  assert s.generate(2) == [[1],[1,1]]
  assert s.generate(3) == [[1],[1,1],[1,2,1]]
  assert s.generate(4) == [[1],[1,1],[1,2,1],[1,3,3,1]]
  assert s.generate(5) == [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
