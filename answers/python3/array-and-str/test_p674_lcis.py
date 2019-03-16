# coding: utf-8

__author__ = '代码会说话'

"""
给定一个未经排序的整数数组，找到最长且连续的的递增序列。

示例 1:

输入: [1,3,5,4,7]
输出: 3
解释: 最长连续递增序列是 [1,3,5], 长度为3。
尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为5和7在原数组里被4隔开。 
示例 2:

输入: [2,2,2,2,2]
输出: 1
解释: 最长连续递增序列是 [2], 长度为1。
注意：数组长度不会超过10000。
"""

from typing import List


class Solution:
  def findLengthOfLCIS(self, nums: List[int]) -> int:
    N = len(nums)
    if N < 2:
      return N
    max_len = 0
    prev_num = nums[0]
    lo = 0
    for i in range(1, N):
      num = nums[i]
      if num <= prev_num:
        cur_len = i - lo
        max_len = max(max_len, cur_len)
        lo = i
      prev_num = num
    max_len = max(max_len, N - lo)
    return max_len


def test():
  s = Solution()
  assert s.findLengthOfLCIS(nums=[1, 3, 5, 4, 7, 8, 9]) == 4
  assert s.findLengthOfLCIS(nums=[1, 3, 5, 4, 7]) == 3
  assert s.findLengthOfLCIS(nums=[2, 2, 2, 2, 2]) == 1
