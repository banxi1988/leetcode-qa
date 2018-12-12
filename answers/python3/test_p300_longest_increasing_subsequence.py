# coding: utf-8
import bisect
import functools

__author__ = '代码会说话'

"""
LeetCode 300. 最长上升子序列 从递归解法到动态规划详解 
by 代码会说话

给定一个无序的整数数组，找到其中最长上升子序列的长度。
备注：子序列不是子数组

示例:

输入: [2,5,3,4]
输出: 3 
解释: 最长的上升子序列是 [2,3,4]，它的长度是 3。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
"""
from typing import List

class Solution:
  def lengthOfLIS(self, nums:List[int]) -> int:
    n = len(nums)
    if not n:
      return 0
    brothers = [0] * n
    brothers[0] = 1
    max_count = 0
    for i in range(1,n):
      bro_count = 0
      ival = nums[i]
      for j in range(0,i):
        jval = nums[j]
        if jval < ival:
           bro_count = max(bro_count,brothers[j])
      bro_count += 1
      brothers[i] = bro_count
      max_count = max(max_count, bro_count)
    return max_count










def test():
  s = Solution()
  assert s.lengthOfLIS([2,5,3,4]) == 3
  assert s.lengthOfLIS([10,9,2,5,3,1,4]) == 3
  assert s.lengthOfLIS([0,8,4,12,2]) == 3
  assert s.lengthOfLIS([10,9,2,1,3,4]) == 3
  assert s.lengthOfLIS([10,9,2,5,3,6,4,5]) == 4
  assert s.lengthOfLIS([10,9,2,5,3,7,101,18]) == 4
  assert s.lengthOfLIS([10,4,9,2,5,3,7,101,18]) == 4
