# coding: utf-8

__author__ = '代码会说话'

"""
给定 N，想象一个凸 N 边多边形，其顶点按顺时针顺序依次标记为 A[0], A[i], ..., A[N-1]。

假设您将多边形剖分为 N-2 个三角形。对于每个三角形，该三角形的值是顶点标记的乘积，三角剖分的分数是进行三角剖分后所有 N-2 个三角形的值之和。

返回多边形进行三角剖分后可以得到的最低分。
 

示例 1：

输入：[1,2,3]
输出：6
解释：多边形已经三角化，唯一三角形的分数为 6。
示例 2：



输入：[3,7,4,5]
输出：144
解释：有两种三角剖分，可能得分分别为：3*7*5 + 4*5*7 = 245，或 3*4*5 + 3*4*7 = 144。最低分数为 144。
示例 3：

输入：[1,3,1,4,1,5]
输出：13
解释：最低分数三角剖分的得分情况为 1*1*3 + 1*1*4 + 1*1*5 + 1*1*1 = 13。
 

提示：

3 <= A.length <= 50
1 <= A[i] <= 100
"""

from typing import List
from functools import lru_cache
class Solution:

  def minScoreTriangulation(self, A: List[int]) -> int:
    arr = ",".join(str(e) for e in A)
    return self.minScoreMemo(arr)

  @lru_cache(maxsize=None)
  def minScoreMemo(self, arr: str) -> int:
    A = [int(e) for e in arr.split(",")]
    N = len(A)
    def min_score(i:int):
      sums = 0
      vi = A[i]
      for no in range(N-2):
        j = (i + no + 1) % N
        k = (j + 1) % N
        sums += (vi * A[j] * A[k])
      return sums
    if N <= 5:
      return min(min_score(i) for i in range(N))
    min_scores = []
    for i in range(N):
      j = (i +1) % N
      k = (i -1 + N) % N
      a_copy = list(A)
      a_copy.pop(i)
      score = A[i] * A[j] * A[k]
      score += self.minScoreTriangulation(a_copy)
      min_scores.append(score)

    return min(min_scores)



def test():
  s = Solution()
  assert s.minScoreTriangulation(A=[1,2,3]) == 6
  assert s.minScoreTriangulation(A=[3,7,4,5]) == 144
  assert s.minScoreTriangulation(A=[1,3,1,4,1,5]) == 13

  assert s.minScoreTriangulation([35,73,90,27,71,80,21,33,33,13,48,12,68,70,80,36,66,3,70,58]) == 13
