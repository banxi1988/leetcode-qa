# coding: utf-8

__author__ = '代码会说话'

"""
962. 最大宽度坡

给定一个整数数组 A，坡是元组 (i, j)，其中  i < j 且 A[i] <= A[j]。这样的坡的宽度为 j - i。

找出 A 中的坡的最大宽度，如果不存在，返回 0 。

 

示例 1：

输入：[6,0,8,2,1,5]
输出：4
解释：
最大宽度的坡为 (i, j) = (1, 5): A[1] = 0 且 A[5] = 5.
示例 2：

输入：[9,8,1,0,1,9,4,0,4,1]
输出：7
解释：
最大宽度的坡为 (i, j) = (2, 9): A[2] = 1 且 A[9] = 1.
"""

from typing import List
class Solution:
  def maxWidthRamp(self, A:List[int]) -> int:
    num_len = len(A)
    total_max = 0
    i = 0
    while i < (num_len - total_max):
      max_width = 0
      ai = A[i]
      j = i + 1
      while j < (num_len):
        if A[j] >= ai:
          max_width = max(max_width, j -i)
        j += 1
      total_max = max(total_max,max_width)
      i += 1

    return total_max


def test():
  s = Solution()
  assert s.maxWidthRamp([6,0,8,2,1,5]) == 4
  assert s.maxWidthRamp([9,8,1,0,1,9,4,0,4,1]) == 7
