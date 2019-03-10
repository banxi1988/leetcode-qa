# coding: utf-8

__author__ = '代码会说话'

"""
在一排多米诺骨牌中，A[i] 和 B[i] 分别代表第 i 个多米诺骨牌的上半部分和下半部分。（一个多米诺是两个从 1 到 6 的数字同列平铺形成的 —— 该平铺的每一半上都有一个数字。）

我们可以旋转第 i 张多米诺，使得 A[i] 和 B[i] 的值交换。

返回能使 A 中所有值或者 B 中所有值都相同的最小旋转次数。

如果无法做到，返回 -1.

 

示例 1：



输入：A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
输出：2
解释：
图一表示：在我们旋转之前， A 和 B 给出的多米诺牌。
如果我们旋转第二个和第四个多米诺骨牌，我们可以使上面一行中的每个值都等于 2，如图二所示。
示例 2：

输入：A = [3,5,1,2,3], B = [3,6,3,3,4]
输出：-1
解释：
在这种情况下，不可能旋转多米诺牌使一行的值相等。
 
 [i,j,k,...]

提示：

1 <= A[i], B[i] <= 6
2 <= A.length == B.length <= 20000
"""

from typing import List

from collections import defaultdict


class Solution:
  def minDominoRotations(self, A: List[int], B: List[int]) -> int:
    a_num_to_indexes = defaultdict(list)
    for i, num in enumerate(A):
      a_num_to_indexes[num].append(i)

    b_num_to_indexes = defaultdict(list)
    for i, num in enumerate(B):
      b_num_to_indexes[num].append(i)

    a_set = set(a_num_to_indexes.keys())
    b_set = set(b_num_to_indexes.keys())
    if len(a_set) == 1 or len(b_set) == 1:
      return 0

    min_count = 20001
    for num in a_set:
      rot_count = 0
      possible = True
      for numo, indexes in a_num_to_indexes.items():
        if numo == num:
          continue
        if all(B[i] == num for i in indexes):
          rot_count += len(indexes)
        else:
          possible = False
          break
      if possible:
        min_count = min(min_count, rot_count)

    for num in b_set:
      rot_count = 0
      possible = True
      for numo, indexes in b_num_to_indexes.items():
        if numo == num:
          continue
        if all(A[i] == num for i in indexes):
          rot_count += len(indexes)
        else:
          possible = False
          break
      if possible:
        min_count = min(min_count, rot_count)

    if min_count < 20001:
      return min_count
    else:
      return -1


def test():
  s = Solution()

  assert s.minDominoRotations(A=[2, 1, 2, 4, 2, 2], B=[5, 2, 6, 2, 3, 2]) == 2
  assert s.minDominoRotations(A=[3, 5, 1, 2, 3], B=[3, 6, 3, 3, 4]) == -1
