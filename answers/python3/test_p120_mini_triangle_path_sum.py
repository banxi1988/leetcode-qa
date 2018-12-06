# coding: utf-8

__author__ = "banxi"

"""
LeetCode 120 三角形最小路径和 题解 by @代码会说话

给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

例如，给定三角形：

[
     [2],
     
    [3,4],         [3],[4]
   [6,5,7],  -> [7],[6],[10]
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

  [2]          [2]
 [2,1]  ->   [3] [5]  -> [7]
[1,4,5]
"""

from typing import List


class Solution:

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        levels = len(triangle)
        level = (levels -1) -1 # 从倒数第二个开始累加小三角路径各
        cur_min_sum = triangle[-1]
        while level > -1:
            row = triangle[level] # 2,1
            next_min_sum = list(row)
            for index,num in enumerate(row):
                next_min_sum[index] += min(cur_min_sum[index], cur_min_sum[index+1])

            cur_min_sum = next_min_sum
            level-=1
        return cur_min_sum[0]





def test():
    s = Solution()
    tri = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    assert s.minimumTotal(tri) == 11

    tri2 = [[2], [2, 1]]
    assert s.minimumTotal(tri2) == 3

    tri3 = [[2], [2, 1], [1, 4, 5]]
    assert s.minimumTotal(tri3) == 5


# 42 / 43 个通过测试用例

