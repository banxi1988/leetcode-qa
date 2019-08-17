# coding: utf-8

__author__ = '代码会说话'

"""
4. 寻找两个有序数组的中位数

给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List

class Solution:
  def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    N1 = len(nums1)
    N2 = len(nums2)
    N = N1 + N2
    if N % 2 == 1:
      k = (N+1) //2
      return self.getKth(nums1, nums2,k)
    else:
      k1 = N //2
      k2 = k1 +1
      num1 = self.getKth(nums1, nums2, k1)
      num2 = self.getKth(nums1, nums2, k2)
      return (num1 + num2) * 0.5

  def getKth(self,arr1:List[int],arr2:List[int],k:int):
    # 处理成 arr1 长度小于或等于 arr2
    if len(arr1) > len(arr2):
      arr1,arr2 = arr2,arr1
    N1 = len(arr1)
    N2 = len(arr2)
    if N1 == 0:
      return arr2[k-1]
    if k == 1:
      return min(arr1[0],arr2[0])
    if k == (N1 + N2):
      return max(arr1[-1],arr2[-1])

    # [1,3,4,9]  [1,2,3,4,5,6,7,8,9]  k = 7
    mid1 = min(N1, k//2) -1 # 2 -> 4
    mid2 = min(N2,k//2) -1 # 2 -> 3
    if arr1[mid1] > arr2[mid2]:
      # 以上面示例来说,4 > 3 第 k位数不会存在于 [1,2,3] 之中,排除.
      return self.getKth(arr1,arr2[mid2+1:], k - (mid2+1))
    else:
      return self.getKth(arr1[mid1+1:],arr2, k - (mid1+1))




  def findIncArraysMedian(self,arr1:List[int], arr2:List[int]):
    N1 = len(arr1)
    N2 = len(arr2)
    N = N1 + N2
    mid = N//2
    if N % 2 == 0:
      num1 = arr1[mid] if mid < N1 else arr2[mid -N1]
      mid2 = mid -1
      num2 = arr2[mid] if mid2 < N1 else arr2[mid2 - N1]
      return (num1 + num2) /2
    else:
      if mid < N1:
        return arr1[mid]
      else:
        return arr2[mid - N1]

  def findMedian(self,arr:List[int]):
    N = len(arr)
    mid = N//2
    if N % 2 == 0:
      return (arr[mid] + arr[mid-1]) / 2
    else:
      return arr[mid]

  def mergeSortedArray(self,nums1:List[int],nums2:List[int]):
    N1 = len(nums1)
    N2 = len(nums2)
    arr = [0] * (N1 + N2)
    i = 0
    j = 0
    k = 0
    while i < N1 or j < N2:
      ni,nj  = None,None
      if i < N1:
        ni = nums1[i]
      if j < N2:
        nj = nums2[j]
      if ni and nj:
        if ni < nj:
          arr[k] =ni
          i+=1
        else:
          arr[k] = nj
          j+=1
      elif ni:
        arr[k] = ni
        i+=1
      else:
        arr[k] = nj
        j+=1
      k+=1
    return arr

  def findMedianSortedArrays_v1(self, nums1: List[int], nums2: List[int]) -> float:
    return self.findMedian(self.mergeSortedArray(nums1, nums2))


def test():
  s = Solution()

  assert s.findMedianSortedArrays(nums1=[1],nums2=[]) == 1
  assert s.findMedianSortedArrays(nums1=[1,2],nums2=[]) == 1.5
  assert s.findMedianSortedArrays(nums1=[1,3],nums2=[2]) == 2
  assert s.findMedianSortedArrays(nums1=[1,2],nums2=[3,4]) == 2.5
  assert s.findMedianSortedArrays(nums1=[1,2,3],nums2=[2,3,4]) == 2.5
  assert s.findMedianSortedArrays(nums1=[1,2],nums2=[2,3,4]) == 2
