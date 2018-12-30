# coding: utf-8

__author__ = '代码会说话'
"""
返回所有长度为 N 且满足其每两个连续位上的数字之间的差的绝对值为 K 的非负整数。

请注意，除了数字 0 本身之外，答案中的每个数字都不能有前导零。例如，01 因为有一个前导零，所以是无效的；但 0 是有效的。

你可以按任何顺序返回答案。

 

示例 1：

输入：N = 3, K = 7
输出：[181,292,707,818,929]
解释：注意，070 不是一个有效的数字，因为它有前导零。
示例 2：

输入：N = 2, K = 1
输出：[10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
 

提示：

1 <= N <= 9
0 <= K <= 9
"""

from typing import List
class Solution:


  def numsSameConsecDiff(self, N:int, K:int) -> List[int]:
    if N == 1:
      return list(range(0,10))

    result = []
    def collect_num(num:int ,prevd:int, N: int, diff: int):
      num *= 10
      digit = prevd + diff
      if digit < 0 or digit > 9:
        return
      num += digit
      if N == 1:
        result.append(num)
      else:
        collect_num(num, digit, N -1, -diff)
        if diff != 0:
          collect_num(num, digit, N -1, diff)

    start = list(range(1,10))
    for d1 in start:
        collect_num(d1,d1,N-1,K)
        if K != 0:
          collect_num(d1,d1,N-1,-K)

    return result

def test():
  s = Solution()
  act1 = s.numsSameConsecDiff(3,0)
  act1.sort()
  assert act1 == [111,222,333,444,555,666,777,888,999]
  res1 = s.numsSameConsecDiff(3,1)
  res1.sort()
  exp1 = [101,121,123,210,212,232,234,321,323,343,345,432,434,454,456,543,545,565,567,654,656,676,678,765,767,787,789,876,878,898,987,989]
  assert exp1 == res1
  assert s.numsSameConsecDiff(3,7) == [181,292,707,818,929]
  res2 = s.numsSameConsecDiff(2,1)
  res2.sort()
  assert res2 == [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
  res3 = s.numsSameConsecDiff(2,0)
  res3.sort()
  assert res3 == [11,22,33,44,55,66,77,88,99]
  res4 = s.numsSameConsecDiff(2,9)
  res4.sort()
  assert res4 == [90]
