# coding: utf-8

__author__ = '代码会说话'


class Solution:
  def containsNearbyDuplicate(self, nums, k):
    s = set()
    for i in range(len(nums)):
      if i > k:
        s.remove(nums[i - k - 1])
      num = nums[i]
      if num in s:
        return True
      s.add(num)
    return False

def test():
  s = Solution()

  assert s.containsNearbyDuplicate([1,2,3,1],k = 3)
  assert s.containsNearbyDuplicate([1,0,1,1],k = 1)
  assert s.containsNearbyDuplicate([1,2,3,1,2,3],k = 2) == False
