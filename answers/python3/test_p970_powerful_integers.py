# coding: utf-8

__author__ = '代码会说话'

"""
给定两个非负整数 x 和 y，如果某一整数等于 x^i + y^j，其中整数 i >= 0 且 j >= 0，那么我们认为该整数是一个强整数。

返回值小于或等于 bound 的所有强整数组成的列表。

你可以按任何顺序返回答案。在你的回答中，每个值最多出现一次。

 

示例 1：

输入：x = 2, y = 3, bound = 10
输出：[2,3,4,5,7,9,10]
解释： 
2 = 2^0 + 3^0
3 = 2^1 + 3^0
4 = 2^0 + 3^1
5 = 2^1 + 3^1
7 = 2^2 + 3^1
9 = 2^3 + 3^0
10 = 2^0 + 3^2
示例 2：

输入：x = 3, y = 5, bound = 15
输出：[2,4,6,8,10,14]
 

提示：

1 <= x <= 100
1 <= y <= 100
0 <= bound <= 10^6
"""

from typing import List
class Solution:
  def powerfulIntegers(self, x:int, y:int, bound:int) -> List[int]:
    x_val = 1
    x_list = []
    i = 0
    while x_val <= bound and i < 21:
      x_list.append(x_val)
      x_val *= x
      i+= 1

    y_val = 1
    y_list = []
    j = 0
    while y_val <= bound and j < 21:
      y_list.append(y_val)
      y_val *= y
      j += 1

    val_set = set()
    for x in x_list:
      for y in y_list:
        val = x + y
        if val <= bound:
          val_set.add(val)
        else:
          break

    return list(val_set)





def test():
  s = Solution()
  assert s.powerfulIntegers(1,2, 10) == [9,2,3,5]
  assert s.powerfulIntegers(2,3,10) == [2,3,4,5,7,9,10]

  assert s.powerfulIntegers(3,5, 15) == [2,4,6,8,10,14]

