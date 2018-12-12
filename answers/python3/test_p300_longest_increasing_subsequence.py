# coding: utf-8

__author__ = '代码会说话'

"""
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4 
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
"""
from typing import List

class Solution:
  def lengthOfLIS(self, nums:List[int]) -> bool:
    n = len(nums)
    def llis_from(prev:int,cur_pos:int):
      if cur_pos == n:
        return 0
      taken = 0
      cur = nums[cur_pos]
      if cur > prev:
        taken = 1 + llis_from(cur,cur_pos+1)
      not_taken = llis_from(prev, cur_pos + 1)
      return max(taken, not_taken)
    import sys
    return llis_from(-sys.maxsize -1,0)


def test():
  s = Solution()
  assert s.lengthOfLIS([10,9,2,5,3,4]) == 3
  assert s.lengthOfLIS([10,9,2,5,3,6,4,5]) == 4
  assert s.lengthOfLIS([10,9,2,5,3,7,101,18]) == 4
  assert s.lengthOfLIS([10,4,9,2,5,3,7,101,18]) == 4
