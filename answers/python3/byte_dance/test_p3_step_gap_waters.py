# coding: utf-8
from typing import List

__author__ = '代码会说话'

"""
有一组不同高度的台阶,由一个整数数组表示,数组中每个数是台阶的高度.
当开始下雨了(水足够多),台阶之间的水坑会积多少水呢?

如下图:
可以表示为数组 [0,1,0,2,1,0,1,3,2,1,2,1]
返回积水量 6.


"""

class Solution:
  def calc_waters_v1(self,arr:List[int]):
    N = len(arr)
    i = 0
    j = N -1
    total = 0
    prev_height = 0

    def step_area(height:int):
      size = 0
      for step in arr[i+1:j]:
        if step > prev_height:
          h = min(step, height) - prev_height
          size += h
      return size

    while (j-i) > 1:
      hi = arr[i]
      hj = arr[j]
      height = min(hj,hi)
      if height > prev_height:
        width = j -i -1
        if width > 0:
          area = width * (height -prev_height)
          taked =  step_area(height)
          gap = area - taked
          if gap > 0:
            total += gap
            prev_height = height
        i += 1
        j -= 1
      else:
        if  hi <= prev_height:
          i+=1
        if hj <= prev_height:
          j-=1
    return total

  def calc_waters(self,arr:List[int]):
    N = len(arr)
    if N <= 2:
      return 0
    total_volume = 0
    j = N -1
    max_l = arr[0]
    max_r = 0
    max_rs = [0] * N
    while j > -1:
      max_r = max(arr[j], max_r)
      max_rs[j] = max_r
      j -= 1

    for i in range(1,N):
      hi  = arr[i]
      if hi > max_l:
        max_l = hi

      h = min(max_l, max_rs[i])
      volume = max(h - hi, 0)
      total_volume += volume
    return total_volume






def test():
  s = Solution()
  assert s.calc_waters([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
  assert s.calc_waters([0,1,0,2]) == 1
  assert s.calc_waters([0,1]) == 0
  assert s.calc_waters([0,1,2]) == 0
  assert s.calc_waters([0,1,2,1]) == 0
  assert s.calc_waters([0,2,0,1]) == 1
  assert s.calc_waters([0,1,0,2,1,0,1]) == 2
  assert s.calc_waters([0,1,0,2,0,0,1]) == 3
