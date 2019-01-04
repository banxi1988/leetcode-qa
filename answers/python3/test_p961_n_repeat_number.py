# coding: utf-8

__author__ = '代码会说话'

from typing import List
from collections import Counter
class Solution:
  def repeatedNTimes(self, A:List[int]) -> int:
    counter = Counter(A)
    return counter.most_common(1)[0][0]


def test():
  s = Solution()
  assert s.repeatedNTimes([1,2,3,3]) == 3
  assert s.repeatedNTimes([2,1,2,5,3,2]) == 2
