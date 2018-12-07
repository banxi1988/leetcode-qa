# coding: utf-8

__author__ = '代码会说话'

"""
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
"""

from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        cur_row_path_sum = grid[-1]
        for i in reversed(range(0,n-1)):
            cur_row_path_sum[i] += cur_row_path_sum[i+1]
        for i in reversed(range(0,m-1)):
            row = grid[i]
            for index in reversed(range(0,n)):
                min_num = cur_row_path_sum[index]
                if index < (n-1):
                    min_num = min(min_num, row[index + 1])
                row[index] += min_num
            cur_row_path_sum = row
        return cur_row_path_sum[0]



def test():
    s = Solution()
    grid1 = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    assert s.minPathSum(grid1) == 7
