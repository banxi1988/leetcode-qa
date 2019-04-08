# coding: utf-8

__author__ = '代码会说话'
"""
给定一个整数数组 A，只有我们可以将其划分为三个和相等的非空部分时才返回 true，否则返回 false。

形式上，如果我们可以找出索引 i+1 < j 且满足 (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1]) 就可以将数组三等分。

 

示例 1：

输出：[0,2,1,-6,6,-7,9,1,2,0,1]
输出：true
解释：0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
示例 2：

输入：[0,2,1,-6,6,7,9,-1,2,0,1]
输出：false
示例 3：

输入：[3,3,6,5,-2,2,5,1,-9,4]
输出：true
解释：3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
 

提示：

3 <= A.length <= 50000
-10000 <= A[i] <= 10000

[0,2,1,-6,6,-7,9,1,2,0,1]
[0,2,3,-3,3,-4,5,6,8,8,9]
"""

from typing import List


class Solution:
  def canThreePartsEqualSum(self, A: List[int]) -> bool:
    asum = sum(A)
    if asum % 3 != 0:
      return False
    part_sum = asum // 3

    part_count = 0
    cur_sum = 0
    for num in A:
      cur_sum += num
      if cur_sum == part_sum:
        cur_sum = 0
        part_count += 1
    return part_count == 3


def test():
  s = Solution()
  assert s.canThreePartsEqualSum([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]) == True
  assert s.canThreePartsEqualSum([0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1]) == False
  assert s.canThreePartsEqualSum([3, 3, 6, 5, -2, 2, 5, 1, -9, 4]) == True
