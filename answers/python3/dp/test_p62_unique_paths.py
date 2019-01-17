# coding: utf-8

__author__ = '代码会说话'

"""
LeetCode  62. 不同路径 题解 从递归解法到动态规划 by 代码会说话

一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？



例如，上图是一个7 x 3 的网格。有多少可能的路径？

说明：m 和 n 的值均不超过 100。

示例 1:

输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右

S(m,n) = S(m-1,n) + S(m,n-1)
S(3,2) = S(2,2) + S(3,1) -> S(2,1) + S(1,2) + S(3,1)

示例 2:

输入: m = 7, n = 3
输出: 28

[1][1][1]
[1][0][0]

"""

# 1. 递归
# 2. functools
# 3. DP
class Solution:

    def uniquePaths(self, m:int, n:int) -> int:
        grid = [[0] * m] * n # grid[m][n]
        for row in range(0,n):
            grid[row][0] = 1
        for col in range(0, m):
            grid[0][col] = 1

        for row in range(1,n):
            for col in range(1, m):
                grid[row][col] = grid[row-1][col] + grid[row][col-1]

        return grid[n-1][m-1]




def test():
    s = Solution()
    assert s.uniquePaths(3,2) == 3
    assert s.uniquePaths(7,3) == 28
    s.uniquePaths(50,50)
