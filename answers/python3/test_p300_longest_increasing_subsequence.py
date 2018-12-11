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
    max_len = 0
    for i in range(0,n):
      prev_num = nums[i]
      cur_len = 1
      for j in range(i + 1,n):
        cur_num = nums[j]
        if cur_num > prev_num:
          cur_len+=1
          prev_num = cur_num
      max_len = max(cur_len,max_len)

    return max_len




def test():
  s = Solution()
  assert s.lengthOfLIS([10,9,2,5,3,4]) == 3
  assert s.lengthOfLIS([10,9,2,5,3,7,101,18]) == 4
  assert s.lengthOfLIS([10,4,9,2,5,3,7,101,18]) == 4
