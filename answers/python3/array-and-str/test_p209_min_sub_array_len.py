# coding: utf-8

__author__ = '代码会说话'

"""
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。

示例: 

输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
进阶:

如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。


"""

from typing import  List

class Solution:
  def minSubArrayLen(self, s:int, nums:List[int]):
    num_count = len(nums)
    sums = [0] * (num_count + 1)
    for i,num in enumerate(nums):
      sums[i+1] = sums[i] + num
    for k in range(1, num_count + 1):
      i = 1
      j = k
      while j < (num_count + 1):
        ijsum = sums[j] - sums[i-1]
        if ijsum >= s:
          return k
        i += 1
        j += 1
    return 0




def test():
  s = Solution()
  assert s.minSubArrayLen(s = 11,nums=[1,2,3,4,5]) == 3
  assert s.minSubArrayLen(s = 7, nums = [2,3,1,2,4,3]) == 2
  assert s.minSubArrayLen(s = 15, nums = [2,3,1,2,4,3]) == 6
  assert s.minSubArrayLen(s = 13, nums = [2,3,1,2,4,3]) == 5
