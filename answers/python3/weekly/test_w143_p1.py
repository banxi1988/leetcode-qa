# coding: utf-8
from typing import List

__author__ = '代码会说话'

import math

class Solution:
  def distributeCandies(self, candies: int, num_people: int) -> List[int]:
    ans = [0] * num_people
    i = 0
    c = 1
    while candies > 0:
      if candies >= c:
        ans[i] += c
      else:
        ans[i] += candies
      candies -= c
      i = (i+1)%num_people
      c+=1
    return ans

def test():
  s = Solution()

  assert s.distributeCandies(candies = 7, num_people = 4) == [1,2,3,1]
  assert s.distributeCandies(candies = 10, num_people = 3) == [5,2,3]
