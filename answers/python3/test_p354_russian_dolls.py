# coding: utf-8

__author__ = '代码会说话'

"""
LeetCode 354. 俄罗斯套娃信封问题从 O(n2)到O(nlogn)的解法详解 by 代码会说话

给定一些标记了宽度和高度的信封，宽度和高度以整数对形式 (w, h) 出现。当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。

请计算最多能有多少个信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。

说明:
不允许旋转信封。

示例:

输入: envelopes = [[5,4],[6,4],[6,7],[2,3]]
输出: 3 
解释: 最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。
(2,3) 1
(5,4) 2
(6,4) 2
(6,7) 3

[46,89], 1
[50,53], 1
[52,68], 2
[72,45], 1
[77,81]] 3

[5,6]
[5,7]
[5,8]
[5,9]

[5,9]
[5,8]
[5,7]
[5,6]
[6,8]
[6,10]
[6,8]
"""

from typing import List
import bisect

class Solution(object):
  def lengthOfLIS(self, nums:List[int]) -> int:
    n = len(nums)
    if not n:
      return 0
    lis = []
    for num in nums:
      insert_pos = bisect.bisect_left(lis,num)
      if insert_pos == len(lis):
        lis.append(num)
      else:
        lis[insert_pos] = num
    return len(lis)

  def maxEnvelopes(self, envs:List[List[int]]):
    n = len(envs)
    if n < 2:
      return n

    envs.sort(key=lambda e:(e[0], -e[1]))
    heights = [e[1] for e in envs]
    return self.lengthOfLIS(heights)


def test():
  s = Solution()
  envelopes2 = [[1,15],[7,18],[7,6],[7,100],[2,200],[17,30],[17,45],[3,5],[7,8],[3,6],[3,10],[7,20],[17,3],[17,45]]
  assert s.maxEnvelopes(envelopes2) == 3
  assert s.maxEnvelopes([[46,89],[50,53],[52,68],[72,45],[77,81]]) == 3
  assert s.maxEnvelopes( [[1,1]]) == 1
  envelopes1 = [[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]
  assert s.maxEnvelopes(envelopes1) == 5

  assert s.maxEnvelopes( [[5,4],[6,4],[6,7],[2,3]]) == 3
  assert s.maxEnvelopes( [[5,4],[6,4],[6,5],[6,7],[2,3]]) == 3
  assert s.maxEnvelopes( [[5,4],[6,4]]) == 1
