# coding: utf-8

__author__ = '代码会说话'

"""
环形公交路线上有 n 个站，按次序从 0 到 n - 1 进行编号。我们已知每一对相邻公交站之间的距离，distance[i] 表示编号为 i 的车站和编号为 (i + 1) % n 的车站之间的距离。

环线上的公交车都可以按顺时针和逆时针的方向行驶。

返回乘客从出发点 start 到目的地 destination 之间的最短距离。

提示：

1 <= n <= 10^4
distance.length == n
0 <= start, destination < n
0 <= distance[i] <= 10^4
"""

from typing import List


class Solution:
  def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
    left,right = (start,destination) if start < destination else (destination,start)
    N = len(distance)
    part1 = sum(distance[:left])
    part2 = sum(distance[left:right])
    part3 = sum(distance[right:N-1])
    part4 = distance[N-1]
    return min(part2, part1 + part3 + part4)


def test():
  s = Solution()
  assert s.distanceBetweenBusStops(distance = [1,2,3,4], start = 0, destination = 1) == 1
  assert s.distanceBetweenBusStops(distance = [1,2,3,4], start = 0, destination = 2) == 3
  assert s.distanceBetweenBusStops(distance = [1,2,3,4], start = 0, destination = 3) == 4
