# coding: utf-8

__author__ = '代码会说话'

"""
我们从一块字母板上的位置 (0, 0) 出发，该坐标对应的字符为 board[0][0]。

在本题里，字母板为board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"].

我们可以按下面的指令规则行动：

如果方格存在，'U' 意味着将我们的位置上移一行；
如果方格存在，'D' 意味着将我们的位置下移一行；
如果方格存在，'L' 意味着将我们的位置左移一列；
如果方格存在，'R' 意味着将我们的位置右移一列；
'!' 会把在我们当前位置 (r, c) 的字符 board[r][c] 添加到答案中。
返回指令序列，用最小的行动次数让答案和目标 target 相同。你可以返回任何达成目标的路径。

 

示例 1：

输入：target = "leet"
输出："DDR!UURRR!!DDD!"
示例 2：

输入：target = "code"
输出："RR!DDRR!UUL!R!"
 

提示：

1 <= target.length <= 100
target 仅含有小写英文字母。
"""

from typing import List
from functools import lru_cache
from collections import defaultdict, Counter


class Solution:
  def alphabetBoardPath(self, target: str) -> str:
    BOARD = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
    R = len(BOARD)
    C = len(BOARD[0])
    ch_to_pos = {}
    for r,row in enumerate(BOARD):
      for c,ch in enumerate(row):
        ch_to_pos[ch] = (r,c)
    cur_r = 0
    cur_c = 0
    cmds = []

    def move_by_row(r):
      nonlocal cur_r
      if cur_r < r:
        while cur_r < r:
          cur_r+= 1
          cmds.append('D')
      else:
        while cur_r > r:
          cur_r-= 1
          cmds.append('U')

    def move_by_col(c):
      nonlocal cur_c
      if cur_c < c:
        while cur_c < c:
          cur_c+=1
          cmds.append('R')
      else:
        while cur_c > c:
          cur_c-=1
          cmds.append('L')
    def move_to(r,c):
      nonlocal cur_r,cur_c
      if cur_r == r and cur_c == c:
        return

      if r == (R-1):
        move_by_col(c)
        move_by_row(r)
      else:
        move_by_row(r)
        move_by_col(c)



    for ch in target:
      r,c = ch_to_pos[ch]
      move_to(r,c)
      cmds.append('!')

    return ''.join(cmds)



def test():
  s = Solution()
  assert s.alphabetBoardPath(target="leet") == "DDR!UURRR!!DDD!"
  assert s.alphabetBoardPath(target="code") == "RR!DDRR!UUL!R!"
