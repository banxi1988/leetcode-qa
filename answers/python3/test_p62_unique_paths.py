# coding: utf-8

__author__ = '代码会说话'

class Solution:
    def uniquePaths(self, m:int, n:int) -> int:
        grid = [[0] * m] * n
        for row in range(0,n):
            grid[row][0] = 1
        for col in range(0,m):
            grid[0][col] = 1
        for row in range(1,n):
            for col in range(1,m):
                grid[row][col] = grid[row -1][col] + grid[row][col-1]
        return grid[n-1][m-1]



def test():
    s = Solution()
    assert s.uniquePaths(3,2) == 3
    assert s.uniquePaths(7,3) == 28
