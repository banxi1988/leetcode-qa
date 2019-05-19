# coding: utf-8

__author__ = '代码会说话'

"""
有一堆石头，每块石头的重量都是正整数。

每一回合，从中选出两块最重的石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：

如果 x == y，那么两块石头都会被完全粉碎；
如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
最后，最多只会剩下一块石头。返回此石头的重量。如果没有石头剩下，就返回 0。

 

提示：

1 <= stones.length <= 30
1 <= stones[i] <= 1000
"""

from typing import List
from functools import lru_cache
from collections import defaultdict, Counter
import bisect


class Solution:
  def lastStoneWeight(self, stones: List[int]) -> int:
    stones.sort()
    N = len(stones)
    i = N -1
    while(i > 0):
      y = stones[i]
      x = stones[i-1]
      stones[i] = 0
      stones[i-1] = 0
      weight = y - x
      if weight > 0:
        bisect.insort(stones,weight,hi=i-1)
        i -= 1
      else:
        i -= 2
    return stones[0]


def test():
  s = Solution()
  assert s.lastStoneWeight([9,4,3,2])== 0
  assert s.lastStoneWeight([9,8,4,2])== 1
