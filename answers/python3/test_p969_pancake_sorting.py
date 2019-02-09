# coding: utf-8

__author__ = '代码会说话'

"""
给定数组 A，我们可以对其进行煎饼翻转：我们选择一些正整数 k <= A.length，然后反转 A 的前 k 个元素的顺序。我们要执行零次或多次煎饼翻转（按顺序一次接一次地进行）以完成对数组 A 的排序。

返回能使 A 排序的煎饼翻转操作所对应的 k 值序列。任何将数组排序且翻转次数在 10 * A.length 范围内的有效答案都将被判断为正确。

 

示例 1：

输入：[3,2,4,1]
输出：[4,2,4,3]
解释：
我们执行 4 次煎饼翻转，k 值分别为 4，2，4，和 3。
初始状态 A = [3, 2, 4, 1]
第一次翻转后 (k=4): A = [1, 4, 2, 3]
第二次翻转后 (k=2): A = [4, 1, 2, 3]
第三次翻转后 (k=4): A = [3, 2, 1, 4]
第四次翻转后 (k=3): A = [1, 2, 3, 4]，此时已完成排序。 
示例 2：

3,2,4,1
4,2,3,1
1,3,2,4


输入：[1,2,3]
输出：[]
解释：
输入已经排序，因此不需要翻转任何内容。
请注意，其他可能的答案，如[3，3]，也将被接受。
 

提示：

1 <= A.length <= 100
A[i] 是 [1, 2, ..., A.length] 的排列
"""





from typing import List
class Solution:
  def pancakeSort(self, A:List[int])->List[int]:
    if len(A) == 1:
      return []
    max_num = len(A)
    max_num_index = A.index(max_num)
    k = max_num_index + 1
    A[0:k] = reversed(A[0:k])
    A.reverse()
    return [k , len(A)] + self.pancakeSort(A[:-1])


def pancakeFlip(A:List[int], flips:List[int]) -> List[int]:
  for k in flips:
    A.reverse()
    A[0:k] = reversed(A[0:k])
  return A

def test():
  s = Solution()
  flips1 =  s.pancakeSort([3,2,4,1])
  assert [1,2,3,4] == pancakeFlip([3,2,4,1], flips1)
  flips2 = s.pancakeSort([1,2,3])
  assert [1,2,3] ==  pancakeFlip([1,2,3], flips2)

"""
if len(A) == 1:
    return []
mmax = len(A)
index = A.index(mmax)
A[:index+1] = reversed(A[:index+1])
A.reverse()
return [index+1, len(A)] + self.pancakeSort(A[:-1])

"""