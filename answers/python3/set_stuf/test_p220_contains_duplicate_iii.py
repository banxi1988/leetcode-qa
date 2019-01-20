# coding: utf-8

__author__ = '代码会说话'

"""
给定一个整数数组，判断数组中是否有两个不同的索引 i 和 j，使得 nums [i] 和 nums [j] 的差的绝对值最大为 t，并且 i 和 j 之间的差的绝对值最大为 ķ。

示例 1:

输入: nums = [1,2,3,1], k = 3, t = 0
输出: true
示例 2:

输入: nums = [1,0,1,1], k = 1, t = 2
输出: true
示例 3:

输入: nums = [1,5,9,1,5,9], k = 2, t = 3
输出: false
"""

from typing import List
import sys

class Solution:
  def containsNearbyAlmostDuplicate(self, nums:List[int], k:int, t:int) -> bool:
    if k < 1 or t < 0:
      return False
    bucket_to_num = {}
    int_min = -sys.maxsize -1
    bucket_size = t + 1
    for i,num in enumerate(nums):
      renum = num - int_min
      bucket = renum // bucket_size
      prebucket_num = bucket_to_num.get(bucket -1)
      nextbucket_num = bucket_to_num.get(bucket + 1)
      if bucket in bucket_to_num or (prebucket_num and renum - prebucket_num <= t) or (nextbucket_num and nextbucket_num - renum <=t):
        return True
      if len(bucket_to_num) >= k:
        lastBucket = (nums[i -k ] - int_min) // bucket_size
        del bucket_to_num[lastBucket]
      bucket_to_num[bucket] = renum
    return False


def test():
  s = Solution()
  assert s.containsNearbyAlmostDuplicate([1,5,9,1,5,9], k = 2,t =3) == False
  assert s.containsNearbyAlmostDuplicate([2,6,9,4],k =2, t=2)
  assert s.containsNearbyAlmostDuplicate([1,2,3,1],k = 3,t = 0)
  assert s.containsNearbyAlmostDuplicate([1,0,1,1], k = 1,t =2)
