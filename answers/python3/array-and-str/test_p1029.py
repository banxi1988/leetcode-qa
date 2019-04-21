# coding: utf-8

__author__ = '代码会说话'

"""
公司计划面试 2N 人。第 i 人飞往 A 市的费用为 costs[i][0]，飞往 B 市的费用为 costs[i][1]。

返回将每个人都飞到某座城市的最低费用，要求每个城市都有 N 人抵达。

 

示例：

输入：[[10,20],[30,200],[400,50],[30,20]]
输出：110
解释：
第一个人去 A 市，费用为 10。
第二个人去 A 市，费用为 30。
第三个人去 B 市，费用为 50。
第四个人去 B 市，费用为 20。

最低总费用为 10 + 30 + 50 + 20 = 110，每个城市都有一半的人在面试。
 

提示：

1 <= costs.length <= 100
costs.length 为偶数
1 <= costs[i][0], costs[i][1] <= 1000
"""

from typing import List

from functools import lru_cache


class Solution:
  def twoCitySchedCost(self, costs: List[List[int]]) -> int:

    @lru_cache(maxsize=None)
    def buy(i, aN: int, bN: int):
      if aN == 0 and bN == 0:
        return 0
      if aN == 0:
        return costs[i][1] + buy(i + 1, aN, bN - 1)
      if bN == 0:
        return costs[i][0] + buy(i + 1, aN - 1, bN)
      cost1 = costs[i][0] + buy(i + 1, aN - 1, bN)
      cost2 = costs[i][1] + buy(i + 1, aN, bN - 1)
      return min(cost1, cost2)

    N = len(costs) // 2
    min_costs = buy(0, N, N)
    return min_costs


def test():
  s = Solution()
  assert s.twoCitySchedCost([[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]) == 1859
  assert s.twoCitySchedCost([[10, 20], [30, 200], [400, 50], [30, 20]]) == 110
