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
"""

from typing import List
from collections import defaultdict

class Solution:
  def maxEnvelopes(self, envelopes:List[List[int]]) -> int:
    w_to_h = defaultdict(list)
    h_to_w = defaultdict(list)
    for w,h in envelopes:
      w_to_h[w].append(h)
      h_to_w[h].append(w)
    # for h_list in w_to_h.values():
    #   h_list.sort()
    # for w_list in h_to_w.values():
    #   w_list.sort()
    widths = sorted(w_to_h.keys())
    heights = sorted(h_to_w.keys())
    wi = 0
    pairs = set()
    prev_hi = 0
    w_count = len(widths)
    h_count = len(heights)
    while wi < w_count:
      hi = prev_hi
      w = widths[wi]
      while hi < h_count:
        h = heights[hi]
        ws = h_to_w[h]
        if w in ws:
          pairs.add((w,h))
          prev_hi = hi + 1
          break
        hi += 1
      wi += 1

    return len(pairs)



def test():
  s = Solution()
  envelopes1 = [[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]
  assert s.maxEnvelopes(envelopes1) == 5
  assert s.maxEnvelopes( [[5,4],[6,4],[6,7],[2,3]]) == 3
  assert s.maxEnvelopes( [[5,4],[6,4]]) == 1
