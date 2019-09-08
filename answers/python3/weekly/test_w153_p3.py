# coding: utf-8

__author__ = '代码会说话'

"""
[LeetCode ]. 删除一次得到子数组最大和(难度:中等)

Maximum Subarray Sum with One Deletion

给你一个整数数组，返回它的某个 非空 子数组（连续元素）在执行一次可选的删除操作后，所能得到的最大元素总和。

换句话说，你可以从原数组中选出一个子数组，并可以决定要不要从中删除一个元素（只能删一次哦），
(删除后）子数组中至少应当有一个元素，然后该子数组（剩下）的元素总和是所有子数组之中最大的。

注意，删除一个元素后，子数组 不能为空。

请看示例：

示例 1：

输入：arr = [1,-2,0,3]
输出：4
解释：我们可以选出 [1, -2, 0, 3]，然后删掉 -2，这样得到 [1, 0, 3]，和最大。
示例 2：

输入：arr = [1,-2,-2,3]
输出：3
解释：我们直接选出 [3]，这就是最大和。
示例 3：

输入：arr = [-1,-1,-1,-1]
输出：-1
解释：最后得到的子数组不能为空，所以我们不能选择 [-1] 并从中删去 -1 来得到 0。
     我们应该直接选择 [-1]，或者选择 [-1, -1] 再从中删去一个 -1。

NUM: [1, -2,  0,  3]
SUM: [1, 1, 1,    4]
DEL: [ ,-2 ,-2, -2]

NUM: [8,-1,6, -7,-4, 5,-4,7,-6]
SUM: [8, 8,14,13, 9, 14,10,17,11]
DEL: [ ,-1,-1,-7,-7, -7,-7,-7,-7]

                          15, 24, 28
NUM: [11,-10,-11, 8,  7,  -6, 9,  4,  11,6,5,0]
SUM: [11,11, 1,   9, 16,  10, 19, 23
SUM: [11,1,-10,   8, 15,  15 
DEL: [, -10,-11,-11, -11, -11,-11,-11
        

提示：

1 <= arr.length <= 10^5
-10^4 <= arr[i] <= 10^4

"""

from typing import List

class Solution:
  def maximumSum(self, nums: List[int]) -> int:
    N = len(nums)
    base_maxsums = [0] * N
    base_maxsums[0] = nums[0]
    for i in range(1,N):
      num = nums[i]
      prev_sum = base_maxsums[i- 1]
      if prev_sum >= 0:
        base_maxsums[i] = prev_sum + num
      else:
        base_maxsums[i] = num

    maxsums = [0] * N
    maxsums[0] = nums[0]
    for i in range(1,N):
      prev_sum = maxsums[i-1]
      prev_base_sum = base_maxsums[i-1]
      num = nums[i]
      if prev_sum >= 0:
        if num >= 0:
          maxsums[i] = prev_sum + num
        else:
          maxsums[i] = max(prev_base_sum, prev_sum + num)
      else:
        maxsums[i] = num
    return max(maxsums)



def test():
  s = Solution()
  assert s.maximumSum([1,-2,0,3]) == 4
  assert s.maximumSum([1,-2]) == 1
  assert s.maximumSum([1,-2,-2,0,3]) == 3
  assert s.maximumSum([1,-2,-2,3]) == 3
  assert s.maximumSum([-1,-1,-1,-1]) == -1
  assert s.maximumSum([8,-1,6,-7,-4,5,-4,7,-6]) == 17
  assert s.maximumSum([11,-10,-11,8,7,-6,9,4,11,6,5,0]) == 50
