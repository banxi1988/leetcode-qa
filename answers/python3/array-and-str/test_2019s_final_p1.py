# coding: utf-8

__author__ = '代码会说话'

from typing import List


class Solution:
  def missingElement(self, nums: List[int], k: int) -> int:
    start = nums[0]
    missing_count = 0
    prev_num = start
    N = len(nums)
    for i in range(1, N):
      num = nums[i]
      if num > prev_num + 1:
        old_missing_count = missing_count
        missing_count += num - prev_num - 1
        if missing_count >= k:
          return prev_num + (k - old_missing_count)
      prev_num = num

    return prev_num + (k - missing_count)


def test():
  s = Solution()
  assert s.missingElement(nums=[1, 3, 5], k=2) == 4
  assert s.missingElement(nums=[1, 3, 5], k=3) == 6
  assert s.missingElement(nums=[4, 7, 9, 10], k=1) == 5
  assert s.missingElement(nums=[1, 2, 4], k=3) == 6
  assert s.missingElement(nums=[4, 7, 9, 10], k=3) == 8
