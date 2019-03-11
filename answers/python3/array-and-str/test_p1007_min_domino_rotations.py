# coding: utf-8

__author__ = '代码会说话'

"""
1007. 行相等的最少多米诺旋转

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
 
A = [2,1,2,4,2,2]
B = [5,2,6,2,3,2]

A:
2:[0,2,4,5]
1:[1]
4:[3]

A = [2,2,2,2,2,2]  -> 2
B = [5,1,6,4,3,2]

A = [5,1,6,4,3,2]  -> 3
B = [2,2,2,2,2,2]


A = [3,5,1,2,3]
B = [3,6,3,3,4]

3:[0,4]
5:[1]

提示：

1 <= A[i], B[i] <= 6
2 <= A.length == B.length <= 20000
"""

from typing import List

from collections import Counter, defaultdict

class Solution:
  def minDominoRotations(self, A: List[int], B: List[int]) -> int:
    a_num_to_indexes = defaultdict(list)
    for i, num in enumerate(A):
      a_num_to_indexes[num].append(i)
    b_num_to_indexes = defaultdict(list)
    for i, num in enumerate(B):
      b_num_to_indexes[num].append(i)

    def check_possible(t_num_to_indexes: defaultdict, s: List[int]):
      t_nums = list(t_num_to_indexes.keys())
      t_nums.sort(key=lambda num: len(t_num_to_indexes[num]), reverse=True)
      for target in t_nums:
        possible = True
        rotate_count = 0
        for num in t_nums:
          if num == target:
            continue
          indexes = t_num_to_indexes[num]
          if all(s[i] == target for i in indexes):
            rotate_count += len(indexes)
          else:
            possible = False
            break
        if possible:
          return rotate_count

    min_count = 20001
    count1 = check_possible(a_num_to_indexes, B)
    if count1 is not None:
      min_count = min(min_count, count1)

    count2 = check_possible(b_num_to_indexes, A)
    if count2 is not None:
      min_count = min(min_count, count2)
    if min_count < 20001:
      return min_count
    else:
      return -1


def test():
  s = Solution()

  assert s.minDominoRotations(A=[1, 2, 1, 1, 1, 2, 2, 2], B=[2, 1, 2, 2, 2, 2, 2, 2]) == 1
  assert s.minDominoRotations(A=[2, 1, 2, 4, 2, 2], B=[5, 2, 6, 2, 3, 2]) == 2
  assert s.minDominoRotations(A=[3, 5, 1, 2, 3], B=[3, 6, 3, 3, 4]) == -1
  assert s.minDominoRotations(A=[1, 1, 1], B=[1, 1, 1]) == 0
