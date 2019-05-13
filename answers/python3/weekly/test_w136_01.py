# coding: utf-8

__author__ = '代码会说话'

"""
[LeetCode 第136期周赛]第1题[4分题]

在无限的平面上，机器人最初位于 (0, 0) 处，面朝北方。机器人可以接受下列三条指令之一：

"G"：直走 1 个单位
"L"：左转 90 度
"R"：右转 90 度
机器人按顺序执行指令 instructions，并一直重复它们。

只有在平面中存在圆使得机器人永远无法离开圆时，返回 true。否则，返回 false。

 

示例 1：

输入："GGLLGG"
输出：true
解释：
机器人从 (0,0) 移动到 (0,2)，转 180 度，然后回到 (0,0)。
重复指令时，机器人将保持在以原点为中心，2 为半径的圆中。
示例 2：

输入："GG"
输出：false
解释：
机器人无限向北移动。
示例 3：

输入："GL"
输出：true
解释：
机器人按 (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ... 进行移动。
 

提示：

1 <= instructions.length <= 100
instructions[i] 在 {'G', 'L', 'R'} 中

LR
LLLL

 ->
| _ |
  

1. 当只有 G 时,说明不会在圆中.
2. 当没有 G 时,说明会在圆中.
3. 当只有 L 或 R 时,会在来圆中.
4. 当有G,有L,有R:
   lcnt = lcnt % 4
   rcnt = rcnt % 4
   lcnt == rcnt
  

"""

from typing import List
from functools import lru_cache
from collections import defaultdict, Counter


class Solution:
  def isRobotBounded(self, instructions: str) -> bool:
    gcnt = instructions.count('G')
    lcnt = instructions.count('L')
    rcnt = instructions.count('R')
    if gcnt == 0:
      return True
    if lcnt == 0 and rcnt == 0:
      return False
    else:
      if lcnt > 0 and rcnt > 0:
        lcnt = lcnt % 4
        rcnt = rcnt % 4
        return lcnt != rcnt
      else:
        return True


def test():
  s = Solution()
  assert s.isRobotBounded("GGRGGRGGRGGR") == True
  assert s.isRobotBounded("LLLRLLLRLLGLLGGRGLLLGGLRRRRRGLRLRLRLGGRGRGRLLLLLLGLLRLGLGLRLGGGRR") == False
  assert s.isRobotBounded("GGLLGG") == True
  assert s.isRobotBounded("GL") == True
  assert s.isRobotBounded("GG") == False
  assert s.isRobotBounded("LRRRRLLLRL") == True
