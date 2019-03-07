# coding: utf-8

__author__ = '代码会说话'

"""
15. 三数之和

给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

from typing import List


class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    N = len(nums)
    if N < 3:
      return []
    nums.sort()
    results = set()
    for i in range(N - 2):
      a = nums[i]
      if i > 0 and a == nums[i - 1]:
        continue
      if a > 0:
        break
      lo = i + 1

      hi = N - 1
      while lo < hi:
        b = nums[lo]
        c = nums[hi]
        if b + c == -a:
          results.add((a, b, c))
          lo += 1
          hi -= 1
        elif b + c > -a:
          hi -= 1
        else:
          lo += 1

    return results
    # return [list(t) for t in results]


def test():
  s = Solution()
  assert s.threeSum([-1, 0, 1, 2, -1, -4]) == {
    (-1, 0, 1),
    (-1, -1, 2)
  }
  return
  assert s.threeSum([0, 0, 0, 0, 0]) == {(0, 0, 0)}
  assert s.threeSum([-4, -4, -3, -2, -1, 0, 1, 2, 3, 4, 8]) == {
    (-4, -4, 8),
    (-4, 0, 4),
    (-4, 1, 3),
    (-3, -1, 4),
    (-3, 0, 3),
    (-3, 1, 2),
    (-2, -1, 3),
    (-2, 0, 2),
    (-1, 0, 1)
  }
