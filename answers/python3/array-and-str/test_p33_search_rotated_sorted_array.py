# coding: utf-8

__author__ = '代码会说话'

"""
33. 搜索旋转排序数组

假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
示例 2:

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1

0...N
0..ij..N
j...N0..i

[0,1,2,3,4,5,6]


[4,5,6,7,0,1,2]

midnum = 7
target = 0

"""

from typing import List


class Solution:
  def search(self, nums: List[int], target: int) -> int:
    lo = 0
    hi = len(nums) - 1
    while lo <= hi:
      mid = (lo + hi) // 2
      midnum = nums[mid]
      if target == midnum:
        return mid
      lonum = nums[lo]
      hinum = nums[hi]

      if midnum >= lonum:
        # midnum 在大子数组区域
        if target < midnum:
          if target >= lonum:
            hi = mid - 1
          else:
            lo = mid + 1
        else:
          lo = mid + 1
      else:
        # midnum 在小子数组区域
        if target < midnum:
          hi = mid - 1
        else:
          if target > hinum:
            hi = mid - 1
          else:
            lo = mid + 1

    return -1


def test():
  s = Solution()
  assert s.search(nums=[5, 1, 2, 3, 4], target=1) == 1
  assert s.search(nums=[], target=1) == -1
  assert s.search(nums=[1], target=1) == 0
  assert s.search(nums=[1], target=0) == -1
  assert s.search(nums=[8, 9, 2, 3, 4], target=9) == 1
  assert s.search(nums=[5, 1, 2, 3, 4], target=5) == 0
  assert s.search(nums=[5, 1, 2, 3, 4], target=1) == 1
  assert s.search(nums=[5, 1, 2, 3, 4], target=2) == 2
  assert s.search(nums=[5, 1, 2, 3, 4], target=3) == 3
  assert s.search(nums=[5, 1, 2, 3, 4], target=4) == 4
  assert s.search(nums=[4, 5, 6, 7, 0, 1, 2], target=4) == 0
  assert s.search(nums=[4, 5, 6, 7, 0, 1, 2], target=5) == 1
  assert s.search(nums=[4, 5, 6, 7, 0, 1, 2], target=6) == 2
  assert s.search(nums=[4, 5, 6, 7, 0, 1, 2], target=7) == 3
  assert s.search(nums=[4, 5, 6, 7, 0, 1, 2], target=0) == 4
  assert s.search(nums=[4, 5, 6, 7, 0, 1, 2], target=1) == 5
  assert s.search(nums=[4, 5, 6, 7, 0, 1, 2], target=2) == 6
  assert s.search(nums=[4, 5, 6, 7, 0, 1, 2], target=3) == -1
  assert s.search(nums=[4, 5, 6, 7, 0, 1, 2], target=-1) == -1
  assert s.search(nums=[4, 5, 6, 7, 0, 1, 2], target=8) == -1

  assert s.search(nums=[4, 5, 6, 7, 8, 1, 2, 3], target=4) == 0
  assert s.search(nums=[4, 5, 6, 7, 8, 1, 2, 3], target=5) == 1
  assert s.search(nums=[4, 5, 6, 7, 8, 1, 2, 3], target=6) == 2
  assert s.search(nums=[4, 5, 6, 7, 8, 1, 2, 3], target=7) == 3
  assert s.search(nums=[4, 5, 6, 7, 8, 1, 2, 3], target=8) == 4
  assert s.search(nums=[4, 5, 6, 7, 8, 1, 2, 3], target=1) == 5
  assert s.search(nums=[4, 5, 6, 7, 8, 1, 2, 3], target=2) == 6
  assert s.search(nums=[4, 5, 6, 7, 8, 1, 2, 3], target=3) == 7
  assert s.search(nums=[4, 5, 6, 7, 8, 1, 2, 3], target=0) == -1
  assert s.search(nums=[4, 5, 6, 7, 8, 1, 2, 3], target=9) == -1
