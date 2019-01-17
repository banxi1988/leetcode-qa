# coding: utf-8

__author__ = '代码会说话'

"""
LeetCode 64. 最小路径和

给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。

[
  [7,6,3],
  [7,5,2],
  [7,3,1]
]
"""

from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        for row in range(rows -2, -1, -1):
            grid[row][-1] += grid[row +1][-1]
        for col in range(cols -2, -1, -1):
            grid[-1][col] += grid[-1][col + 1]

        for row in range(rows -2, -1, -1):
            for col in range(cols -2, -1, -1):
                grid[row][col] += min(grid[row +1][col], grid[row][col+1])
        return grid[0][0]





def test():
    s = Solution()
    grid1 = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    assert s.minPathSum(grid1) == 7
