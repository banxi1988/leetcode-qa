# coding: utf-8

__author__ = '代码会说话'

"""
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。
"""

from typing import List
class Solution:
  def plusOne(self, digits:List[int]) -> List[int]:
    carry = 1
    i = len(digits) -1
    while i != -1:
      sum = digits[i] + carry
      digits[i] = sum % 10
      carry = 1 if sum > 9 else 0
      if not carry:
        break
      i-= 1

    if carry:
      digits.insert(0,carry)
    return digits

def test():
  s = Solution()
  assert s.plusOne([0]) == [1]
  assert s.plusOne([9]) == [1,0]
  assert s.plusOne([9,9]) == [1,0,0]
  assert s.plusOne([4,3,2,1]) == [4,3,2,2]
  assert s.plusOne([1,2,3]) == [1,2,4]

