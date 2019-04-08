# coding: utf-8

__author__ = '代码会说话'
"""
给定正整数 K，你需要找出可以被 K 整除的、仅包含每位上都是数字 1 的最小的正整数 N。

返回 N 的长度。如果不存在这样的 N，就返回 -1。

 

示例 1：

输入：1
输出：1
解释：最小的答案是 N = 1，其长度为 1。
示例 2：

输入：2
输出：-1
解释：There is no such positive integer N divisible by 2.
示例 3：

输入：3
输出：3
解释：最小的答案是 N = 111，其长度为 3。
 

5 = (2+3)
10
15
20
25
30

提示：

1 <= K <= 10^5
"""


class Solution:
  def smallestRepunitDivByK(self, K: int) -> int:
    if K % 2 == 0:
      return False


def test():
  s = Solution()
  assert s.smallestRepunitDivByK(2) == -1
  assert s.smallestRepunitDivByK(1) == 1
  assert s.smallestRepunitDivByK(3) == 3
