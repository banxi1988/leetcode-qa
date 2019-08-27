# coding: utf-8

__author__ = '代码会说话'

"""
[LeetCode 1167]. 连接棒材的最低费用

为了装修新房，你需要加工一些长度为正整数的棒材 sticks。
如果要将长度分别为 X 和 Y 的两根棒材连接在一起，你需要支付 X + Y 的费用。
由于施工需要，你必须将所有棒材连接成一根。
返回你把所有棒材 sticks 连成一根所需要的最低费用。
注意你可以任意选择棒材连接的顺序。

[1,2,8]
1+8 -> 9
9 + 2 -> 11   -> 20

1+2 -> 3
3+8 -> 11   -> 14


示例 1：

输入：sticks = [2,4,3]
输出：14
解释：先将 2 和 3 连接成 5，花费 5；再将 5 和 4 连接成 9；总花费为 14。
示例 2：

输入：sticks = [1,8,3,5]
输出：30
[1,3,5,8]

1+3 =  4
4 + 5 = 9
8 + 9 = 17

[1,2,2,2]

1+2 = 3
[2,2,3]



提示：

1 <= sticks.length <= 10^4
1 <= sticks[i] <= 10^4
"""

from typing import List

import bisect

class Solution:
  def connectSticks(self, sticks: List[int]) -> int:
    sticks.sort()
    lo = 0
    cost = 0
    while (lo + 1) < len(sticks):
      s1 = sticks[lo]
      s2 = sticks[lo+1]
      stick = s1 + s2
      lo += 2
      bisect.insort(sticks,stick,lo)
      cost += stick
    return cost


def test():
  s = Solution()
  assert s.connectSticks(sticks = [2,4,3]) == 14

  assert s.connectSticks(sticks = [1,8,3,5]) == 30
  assert s.connectSticks([1,2,2,2]) == 14

