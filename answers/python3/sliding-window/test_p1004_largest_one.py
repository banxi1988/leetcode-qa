# coding: utf-8

__author__ = '代码会说话'

"""
1004. 最大连续1的个数 III 滑动窗口与双指针解法

给定一个由若干 0 和 1 组成的数组 A，我们最多可以将 K 个值从 0 变成 1 。

返回仅包含 1 的最长（连续）子数组的长度。


示例 1：

输入：A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
输出：6
解释： 
[1,1,1,0,0,1,1,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 6。
示例 2：

输入：A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
输出：10
解释：
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 10。
 

  
最多包含K个0的最长子数组。

[i,j] -> j - i + 1

输入：A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
[1,1,1,0,0,0,1,1,1,1,0]
[1]
[1,1]
[1,1,1]
[1,1,1,K]
[1,1,1,K,K]
  [1,1,K,K,K]
    [1,K,K,K,1]
      [K,K,K,1,1]
        [K,K,1,1,1]
        [K,K,1,1,1,1]
          [K,1,1,1,1,K]

提示：

1 <= A.length <= 20000
0 <= K <= A.length
A[i] 为 0 或 1 
"""

from typing import List


class Solution:
  def longestOnes(self, A: List[int], K: int) -> int:
    i = 0
    N = len(A)
    for j in range(0, N):
      if A[j] == 0:
        K -= 1
      if K < 0:
        if A[i] == 0:
          K += 1
        i += 1
    return j - i + 1


def test():
  s = Solution()
  assert s.longestOnes(A=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], K=2) == 6
  assert s.longestOnes(A=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], K=3) == 10
  assert s.longestOnes(A=[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], K=3) == 10
  assert s.longestOnes(A=[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], K=1) == 6
  assert s.longestOnes(A=[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], K=2) == 7
  assert s.longestOnes(A=[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], K=3) == 9
