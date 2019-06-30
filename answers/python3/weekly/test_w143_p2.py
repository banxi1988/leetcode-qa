# coding: utf-8
from typing import List

__author__ = '代码会说话'

from math import log2,floor
class Solution:
  def pathInZigZagTree(self, label: int) -> List[int]:
    # row 从1开始算
    row = int(floor(log2(label))) + 1
    ans = []
    while label > 1:
      level = row -1
      ans.insert(0, label)
      prev_row_min = 2**(level -1)
      prev_row_max = 2**level - 1
      r_value = label // 2
      label = (prev_row_min + (prev_row_max - r_value))
      row -=1

    ans.insert(0, 1)
    return ans



def test():
  s = Solution()
  assert s.pathInZigZagTree(14) == [1,3,4,14]
  assert s.pathInZigZagTree(26) == [1,2,6,10,26]
