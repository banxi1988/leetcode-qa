# coding: utf-8

__author__ = '代码会说话'

"""
【位运算】136. 只出现一次的数字

给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1
示例 2:

输入: [4,1,2,1,2]
输出: 4

[2,2,1]

10 
10  
01

10 & 10 > 10 & 01 = 0
10 | 10 > 10 | 01 = 11 
10 ^ 10 > 00 ^ 01 = 01

[4,1,2,1,2]
[4,1,1,2,2]
[4,0,0]
[4,0]

"""

from typing import List


class Solution:
  def singleNumber(self, nums: List[int]):
    ans = 0
    for num in nums:
      ans ^= num
    return ans


def test():
  s = Solution()
  assert s.singleNumber(nums=[2]) == 2
  assert s.singleNumber(nums=[2, 2, 1]) == 1
  assert s.singleNumber(nums=[4, 1, 2, 1, 2]) == 4
