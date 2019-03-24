# coding: utf-8

__author__ = '代码会说话'
"""
1021. 最佳观光组合

给定正整数数组 A，A[i] 表示第 i 个观光景点的评分，并且两个景点 i 和 j 之间的距离为 j - i。

一对景点（i < j）组成的观光组合的得分为（A[i] + A[j] + i - j）：景点的评分之和减去它们两者之间的距离。

返回一对观光景点能取得的最高分。

 

示例：

输入：[8,1,5,2,6]
输出：11
解释：i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11
 
输入：[8,1,5,2,6]

0,1,2,3,4,5
8,1,5,2,6,9
  7,6,5,4,3
      4,3,2
          5

  
5 + 2 -1 = 6
8 + 2 - (3-0) = 7
提示：

2 <= A.length <= 50000
1 <= A[i] <= 1000
"""

from typing import List


class Solution:

  def maxScoreSightseeingPair_brute(self, A: List[int]) -> int:
    # O(N^2)
    # O(N(LogN))
    # O(N)
    N = len(A)
    max_score = 0
    for i in range(0, N):
      scorei = A[i]
      for j in range(i + 1, N):
        scorej = A[j]
        scoreij = scorei + scorej - (j - i)
        max_score = max(max_score, scoreij)

    return max_score

  def maxScoreSightseeingPair(self, A: List[int]) -> int:
    # 0,1,2,3,4,5
    # 8,1,5,2,6,9
    N = len(A)
    prev_best_index = 0
    max_score = 0
    for j in range(1, N):
      prev_best_score = A[prev_best_index] - (j - prev_best_index)
      scorej = A[j]
      max_score = max(max_score, prev_best_score + scorej)
      if prev_best_score < scorej:
        prev_best_index = j
    return max_score


def test():
  s = Solution()
  funcs = (s.maxScoreSightseeingPair_brute, s.maxScoreSightseeingPair)
  for fun in funcs:
    assert fun([8, 1, 5, 2, 6, 9]) == 14
    assert fun([5, 1, 8, 2, 6]) == 12
    assert fun([8, 1, 5, 2, 6]) == 11
    assert fun([5, 1, 8, 2, 6]) == 12
    assert fun([5, 1, 8, 2, 6, 7, 9]) == 15
