# coding: utf-8

__author__ = '代码会说话'

"""
在一个给定的数组nums中，总是存在一个最大元素 。

查找数组中的最大元素是否至少是数组中每个其他数字的两倍。

如果是，则返回最大元素的索引，否则返回-1。

示例 1:

输入: nums = [3, 6, 1, 0]
输出: 1
解释: 6是最大的整数, 对于数组中的其他整数,
6大于数组中其他元素的两倍。6的索引是1, 所以我们返回1.
 

示例 2:

输入: nums = [1, 2, 3, 4]
输出: -1
解释: 4没有超过3的两倍大, 所以我们返回 -1.
 

提示:

nums 的长度范围在[1, 50].
每个 nums[i] 的整数范围在 [0, 99].
"""

from typing import List
class Solution:
  def dominantIndex(self, nums:List[int]) -> int:
    max_i,max_num = 0,-1
    second_num = -1
    for i,num in enumerate(nums):
      if num > max_num:
        second_num = max_num
        max_num = num
        max_i = i
      elif num > second_num:
        second_num = num
    if second_num * 2 > max_num:
        return -1
    return max_i


def test():
  s = Solution()
  assert s.dominantIndex([0,0,3,2]) == -1
  assert s.dominantIndex([3]) == 0
  assert s.dominantIndex([3,6,1,0]) == 1
  assert s.dominantIndex([1,2,3,4]) == -1
