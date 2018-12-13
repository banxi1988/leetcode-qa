# coding: utf-8

__author__ = '代码会说话'

"""
LeetCode 354. 俄罗斯套娃信封问题 题解 by 代码会说话

给定一些标记了宽度和高度的信封，宽度和高度以整数对形式 (w, h) 出现。当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。

请计算最多能有多少个信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。

说明:
不允许旋转信封。

示例:

输入: envelopes = [[5,4],[6,4],[6,7],[2,3]]
输出: 3 
解释: 最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。
(2,3)
(5,4)
(6,4)
(6,7)
"""

from typing import List


class Solution(object):
  def lengthOfLIS(self, envs:List[List[int]]) -> int:
    n = len(envs)
    brothers = [0] * n
    brothers[0] = 1
    max_count = 0
    for i in range(1,n):
      bro_count = 0
      iw,ih = envs[i]
      for j in range(0,i):
        jw,jh = envs[j]
        if jw < iw and jh < ih:
          bro_count = max(bro_count,brothers[j])
      bro_count += 1
      brothers[i] = bro_count
      max_count = max(max_count, bro_count)
    return max_count

  def maxEnvelopes(self, envs:List[List[int]]):
    n = len(envs)
    if n < 2:
      return n
    envs.sort(key=lambda t:(t[0],t[1]))
    return self.lengthOfLIS(envs)



def test():
  s = Solution()
  assert s.maxEnvelopes( [[1,1]]) == 1
  envelopes2 = [[1,15],[7,18],[7,6],[7,100],[2,200],[17,30],[17,45],[3,5],[7,8],[3,6],[3,10],[7,20],[17,3],[17,45]]
  assert s.maxEnvelopes(envelopes2) == 3
  envelopes1 = [[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]
  assert s.maxEnvelopes(envelopes1) == 5

  assert s.maxEnvelopes( [[5,4],[6,4],[6,7],[2,3]]) == 3
  assert s.maxEnvelopes( [[5,4],[6,4],[6,5],[6,7],[2,3]]) == 3
  assert s.maxEnvelopes( [[5,4],[6,4]]) == 1
