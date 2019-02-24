# coding: utf-8

__author__ = '代码会说话'
"""
999. 车的可用捕获量

在一个 8 x 8 的棋盘上，有一个白色车（rook）。也可能有空方块，白色的象（bishop）和黑色的卒（pawn）。它们分别以字符 “R”，“.”，“B” 和 “p” 给出。大写字符表示白棋，小写字符表示黑棋。

车按国际象棋中的规则移动：它选择四个基本方向中的一个（北，东，西和南），然后朝那个方向移动，直到它选择停止、到达棋盘的边缘或移动到同一方格来捕获该方格上颜色相反的卒。另外，车不能与其他友方（白色）象进入同一个方格。

返回车能够在一次移动中捕获到的卒的数量。
"""

from typing import List

class Solution:
  def numRookCaptures(self, board: 'List[List[str]]') -> 'int':
    rr,rc = 0,0
    for r,row in enumerate(board):
      for c,char in enumerate(row):
        if char == 'R':
          rr,rc = r,c
          break
    res = 0
    # 上，下，左，右
    for incrR,incrC in ((-1,0),(1,0),(0,-1),(0,1)):
      r,c = rr,rc
      while True:
        r += incrR
        c += incrC
        if (r < 0 or r > 7) or (c < 0 or c > 7):
          break
        char =  board[r][c]
        if char == 'B':
          break
        if char == 'p':
          res += 1
          break

    return res


def test():
  s = Solution()

  assert s.numRookCaptures([[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]) == 3

  assert s.numRookCaptures([[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]) == 0

  assert s.numRookCaptures([[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]) == 3

