# coding: utf-8

__author__ = '代码会说话'


from typing import List

class Solution:
  def pivotIndex(self, nums:List[int]) ->int:
    num_count = len(nums)
    if not num_count:
      return -1
    if num_count == 1:
      return 0
    total_sum =  sum(nums)
    left_sum = 0
    for i in range(0,num_count):
      right_sum = total_sum - nums[i] - left_sum
      if left_sum == right_sum:
        return i
      left_sum += nums[i]
    return -1


def test():
  s = Solution()
  assert s.pivotIndex([1, 7, 3, 6, 5, 6]) == 3
  assert s.pivotIndex([1,2,3]) == -1
  assert s.pivotIndex([-1,-1,-1,0,1,1]) == 0
  assert s.pivotIndex([]) == -1
  assert s.pivotIndex([1]) == 0
