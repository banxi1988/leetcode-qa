# coding: utf-8

__author__ = '代码会说话'
"""
对于非负整数 X 而言，X 的数组形式是每位数字按从左到右的顺序形成的数组。例如，如果 X = 1231，那么其数组形式为 [1,2,3,1]。

给定非负整数 X 的数组形式 A，返回整数 X+K 的数组形式。

 

示例 1：

输入：A = [1,2,0,0], K = 34
输出：[1,2,3,4]
解释：1200 + 34 = 1234
解释 2：

输入：A = [2,7,4], K = 181
输出：[4,5,5]
解释：274 + 181 = 455
示例 3：

输入：A = [2,1,5], K = 806
输出：[1,0,2,1]
解释：215 + 806 = 1021
示例 4：

输入：A = [9,9,9,9,9,9,9,9,9,9], K = 1
输出：[1,0,0,0,0,0,0,0,0,0,0]
解释：9999999999 + 1 = 10000000000
 

提示：

1 <= A.length <= 10000
0 <= A[i] <= 9
0 <= K <= 10000
如果 A.length > 1，那么 A[0] != 0
"""


from typing import List
from collections import deque
class Solution:
  def addToArrayForm(self, A: 'List[int]', K: 'int') -> 'List[int]':
    nums = deque()
    i = len(A) -1
    carry = 0
    while i > -1 or K > 0:
      d1 = A[i] if i > -1 else 0
      d2 = K % 10
      sum = d1 + d2 + carry
      num = sum % 10
      carry = 1 if sum > 9 else 0
      nums.appendleft(num)
      K = K // 10
      i -= 1

    if carry:
      nums.appendleft(1)

    return list(nums)



def test():
  s = Solution()
  assert s.addToArrayForm(A = [1,2,0,0], K = 34) == [1,2,3,4]
  assert s.addToArrayForm(A = [2,7,4], K = 181) == [4,5,5]
  assert s.addToArrayForm(A = [2,1,5], K = 806) == [1,0,2,1]
  assert s.addToArrayForm(A = [9,9,9,9,9,9,9,9,9,9], K = 1) == [1,0,0,0,0,0,0,0,0,0,0]
