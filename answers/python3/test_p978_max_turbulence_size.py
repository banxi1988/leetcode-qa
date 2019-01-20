# coding: utf-8

__author__ = '代码会说话'

"""
当 A 的子数组 A[i], A[i+1], ..., A[j] 满足下列条件时，我们称其为湍流子数组：

若 i <= k < j，当 k 为奇数时， A[k] > A[k+1]，且当 k 为偶数时，A[k] < A[k+1]；
或 若 i <= k < j，当 k 为偶数时，A[k] > A[k+1] ，且当 k 为奇数时， A[k] < A[k+1]。
也就是说，如果比较符号在子数组中的每个相邻元素对之间翻转，则该子数组是湍流子数组。

返回 A 的最大湍流子数组的长度。

 

示例 1：

输入：[9,4,2,10,7,8,8,1,9]
输出：5
解释：(A[1] > A[2] < A[3] > A[4] < A[5])
示例 2：

输入：[4,8,12,16]
输出：2
示例 3：

输入：[100]
输出：1
 

提示：

1 <= A.length <= 40000
0 <= A[i] <= 10^9
"""

from typing import List
class Solution:
  def maxTurbulenceSize(self, A:List[int]) -> int:
    num_count = len(A)
    i = 0
    max_size = 1
    while i < (num_count - max_size):
      prev = A[i]
      cur = A[i+1]
      if prev == cur:
        i+=1
        continue
      elif cur > prev:
        incr = False
      else:
        incr = True
      prev = cur
      j = i+2
      while j < num_count:
        cur = A[j]
        if prev == cur:
          break
        elif cur > prev:
          if incr:
            incr = not incr
          else:
            break
        else:
          if incr:
            break
          else:
            incr = not incr
        prev = cur
        j+=1

      size = j -i
      i += (size -1)
      max_size = max(size,max_size)

    return max_size

def test():
  s = Solution()
  assert s.maxTurbulenceSize([0,8,45,88,48,68,28,55,17,24]) == 8
  assert s.maxTurbulenceSize([9,4,2,10,7,8,8,1,9]) == 5
  assert s.maxTurbulenceSize([4,8,12,16]) == 2
  assert s.maxTurbulenceSize([100]) == 1

  assert s.maxTurbulenceSize(list(range(40000))) == 2

