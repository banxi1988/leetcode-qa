# coding: utf-8

__author__ = '代码会说话'

from typing import List


class Solution:
  def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
    def distance_to_p0(p):
      return abs(p[0] - r0) + abs(p[1] - c0)

    points = []
    for r in range(R):
      for c in range(C):
        points.append([r, c])

    points.sort(key=lambda p: distance_to_p0(p))
    return points


def test():
  s = Solution()

  assert s.allCellsDistOrder(R=2, C=3, r0=1, c0=2) == [[1, 2], [0, 2], [1, 1], [0, 1], [1, 0], [0, 0]]
