# coding: utf-8

__author__ = '代码会说话'

"""
[LeetCode 1162]. 地图分析(难度:中等,分值:5分)

你现在手里有一份大小为 N x N 的『地图』（网格） grid，
上面的每个『区域』（单元格）都用 0 和 1 标记好了。其中 0 代表海洋，1 代表陆地，你知道距离陆地区域最远的海洋区域是是哪一个吗？
请返回该海洋区域到离它最近的陆地区域的距离。
我们这里说的距离是『曼哈顿距离』（ Manhattan Distance）：(x0, y0) 和 (x1, y1) 这两个区域之间的距离是 |x0 - x1| + |y0 - y1| 。
如果我们的地图上只有陆地或者海洋，请返回 -1。

 
示例 1：


输入：[
[1,0,1],
[0,0,0],
[1,0,1]
]
[0,1,0],
[1,2,1],
[0,1,0]
输出：2
解释： 
海洋区域 (1, 1) 和所有陆地区域之间的距离都达到最大，最大距离为 2。
示例 2：


输入：[
[1,0,0],
[0,0,0],
[0,0,0]
]

[0,1,2],
[1,2,3],
[2,3,4]
输出：4
解释： 
海洋区域 (2, 2) 和所有陆地区域之间的距离都达到最大，最大距离为 4。

 

提示：

1 <= grid.length == grid[0].length <= 100
grid[i][j] 不是 0 就是 1

dp = 
    [0,1,2,1,1,0,1,1,1,0],
    [0,0,1,0,0,0,1,0,0,1],
    [1,0,0,1,0,1,1,0,1,2],
    [0,N,0,N,0,1,N,1,N,N],
    [N,0,N,N,N,0,0,N,0,0],
    [N,N,0,N,N,0,N,0,N,0],
    [N,N,N,0,0,0,0,N,N,0],
    [N,0,N,N,0,N,N,0,N,N],
    [N,N,N,N,N,0,0,0,N,N],
    [0,0,N,0,0,0,0,0,N,N]]

"""

from typing import List


class Solution:
  def maxDistance(self, grid: List[List[int]]) -> int:
    R,C = len(grid),len(grid[0])
    N = R*C + 1
    dp = [[N] * C for _ in range(R)]
    visited = set()
    for r in range(R):
      for c in range(C):
        if grid[r][c] == 1:
          visited.add((r,c))
          dp[r][c] = 0
        else:
          dp[r][c] = N
    CELL_CNT = R * C
    land_cnt = len(visited)
    if land_cnt == 0 or land_cnt == CELL_CNT:
      return -1

    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    max_dis = 0
    while land_cnt < CELL_CNT:
      recent_visited = []
      for (r,c) in visited:
        rc_dis = dp[r][c]
        for dr,dc in dirs:
          nr,nc = r + dr, c + dc
          if 0 <= nr < R and 0<=nc < C:
            dis = dp[nr][nc]
            if dis == N:
              recent_visited.append((nr,nc))
              dp[nr][nc] = rc_dis +1
      visited = recent_visited
      land_cnt += len(recent_visited)
      max_dis += 1
    return  max_dis
    # return max(max(row) for row in dp)











def test():
  s = Solution()
  assert s.maxDistance([[1,0,0],[0,0,0],[0,0,0]]) == 4

  assert s.maxDistance([
    [1,0,0,0,0,1,0,0,0,1],
    [1,1,0,1,1,1,0,1,1,0],
    [0,1,1,0,1,0,0,1,0,0],
    [1,0,1,0,1,0,0,0,0,0],
    [0,1,0,0,0,1,1,0,1,1],
    [0,0,1,0,0,1,0,1,0,1],
    [0,0,0,1,1,1,1,0,0,1],
    [0,1,0,0,1,0,0,1,0,0],
    [0,0,0,0,0,1,1,1,0,0],
    [1,1,0,1,1,1,1,1,0,0]]
  ) == 2

  assert s.maxDistance([[1,0,1],[0,0,0],[1,0,1]]) == 2
  assert s.maxDistance([[0,0,0],[0,0,0],[0,0,0]]) == -1
  assert s.maxDistance([[1,1,1],[1,1,1],[1,1,1]]) == -1
