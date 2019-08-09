# coding: utf-8
from functools import lru_cache

__author__ = '代码会说话'

"""
[LeetCode 1140]. 石子游戏 II (动态规划,7分题)

亚历克斯和李继续他们的石子游戏。
许多堆石子 排成一行，每堆都有正整数颗石子 piles[i]。游戏以谁手中的石子最多来决出胜负。

亚历克斯和李轮流进行，亚历克斯先开始。最初，M = 1。

在每个玩家的回合中，该玩家可以拿走剩下的 前 X 堆的所有石子，
其中 1 <= X <= 2M。然后，令 M = max(M, X)。

游戏一直持续到所有石子都被拿走。

假设亚历克斯和李都发挥出最佳水平，返回亚历克斯可以得到的最大数量的石头。

 

示例：

输入：piles = [2,7,9,4,4]
M=2 -> [1,4]
take(1)

[2]   [7,9.4,4]
[2,7] [9,4,4] 


输出：10
解释：
如果亚历克斯在开始时拿走一堆石子，李拿走两堆，接着亚历克斯也拿走两堆。
在这种情况下，亚历克斯可以拿到 2 + 4 + 4 = 10 颗石子。 

如果亚历克斯在开始时拿走两堆石子，那么李就可以拿走剩下全部三堆石子。
在这种情况下，亚历克斯可以拿到 2 + 7 = 9 颗石子。
所以我们返回更大的 10。 
 

提示：

1 <= piles.length <= 100
1 <= piles[i] <= 10 ^ 4
"""

from typing import List
class Solution:
  def stoneGameII(self, piles: List[int]) -> int:
    N = len(piles)

    @lru_cache(maxsize=None)
    def take(i:int,M:int):
      remain_sum = sum(piles[i:])
      if (i+2*M) >= N:
        return remain_sum
      min_cnt = 10 ** 6 + 1
      for x in range(1,2*M+1):
        next_M = max(x,M)
        l_take_cnt =  take(i+x, M=next_M)
        if l_take_cnt < min_cnt:
          min_cnt = l_take_cnt
      return remain_sum - min_cnt

    return take(i=0,M=1)

def test():
  s = Solution()
  assert s.stoneGameII(piles=[1,2]) == 3
  assert s.stoneGameII(piles=[2,7,9,4,4]) == 10
  assert s.stoneGameII(piles=[2,7,9,4,4,8,9,8,7,9,10,19,29,11,23,13,8,9,7,5,9,8,7,6,8,8,7,6,8,5,1,3,2,1,2]) == 111
