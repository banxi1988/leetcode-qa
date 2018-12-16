# coding: utf-8

__author__ = '代码会说话'

"""
LeetCode 78. 子集

给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

1,2,3
[]
[],[1]
[],[],[2],[1,2]
"""

from typing import List
class Solution:
  def subsets(self, nums:List[int]) -> List[List[int]]:
    sets = [[]]
    for num in nums:
      new_sets = []
      for set in sets:
        new_sets.append(set)
        taken_set = list(set)
        taken_set.append(num)
        new_sets.append(taken_set)
      sets = new_sets
    return sets



def test():
  s = Solution()
  expected1 = [
    [3],
    [1],
    [2],
    [1,2,3],
    [1,3],
    [2,3],
    [1,2],
    []
  ]
  actual1 = s.subsets([1,2,3])
  assert len(actual1) == len(expected1)
  assert all(l in expected1 for l in actual1)
