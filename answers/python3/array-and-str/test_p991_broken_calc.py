# coding: utf-8

__author__ = '代码会说话'
"""
在显示着数字的坏计算器上，我们可以执行以下两种操作：

双倍：将显示屏上的数字乘 2；
递减：将显示屏上的数字减 1 。
最初，计算器显示数字 X。

返回显示数字 Y 所需的最小操作数。

 

示例 1：

输入：X = 2, Y = 3
输出：2
解释：先进行双倍运算，然后再进行递减运算 {2 -> 4 -> 3}.
示例 2：

输入：X = 5, Y = 8
输出：2
解释：先递减，再双倍 {5 -> 4 -> 8}.
示例 3：

输入：X = 3, Y = 10
输出：3
解释：先双倍，然后递减，再双倍 {3 -> 6 -> 5 -> 10}.
示例 4：

输入：X = 1024, Y = 1
输出：1023
解释：执行递减运算 1023 次
 

提示：

1 <= X <= 10^9
1 <= Y <= 10^9
"""

class Solution:
  def brokenCalc(self, X: 'int', Y: 'int') -> 'int':
    if X >= Y:
      return X - Y
    else:
      if Y % 2 == 0:
        return 1 + self.brokenCalc(X, Y//2)
      else:
        return 1 + self.brokenCalc(X, Y + 1)



def test():
  s = Solution()
  assert s.brokenCalc(X =1, Y = 10) == 6
  assert s.brokenCalc(X = 2, Y = 3) == 2
  assert s.brokenCalc(X = 1024, Y = 1) == 1023
  assert s.brokenCalc(X = 3, Y = 10) == 3
  assert s.brokenCalc(X = 5, Y = 8) == 2


#1,2,4,8,16 -> 15,14,13,12,11 10
#1,2,4,3,6,5,10
#1,2,4,8,7,6,5,10