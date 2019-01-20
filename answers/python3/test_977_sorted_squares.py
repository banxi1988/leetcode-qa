# coding: utf-8

__author__ = '代码会说话'


class Solution:
  def sortedSquares(self, A):
    return sorted([x * x  for x in A])

def test():
  s = Solution()
  assert s.sortedSquares([-4,-1,0,3,10]) == [0,1,9,16,100]
  assert s.sortedSquares([-7,-3,2,3,11]) == [4,9,9,49,121]
