# coding: utf-8
from typing import List

__author__ = '代码会说话'

"""
[字节跳动,头条笔试题][LeetCode 42]. 接雨水,积水问题

有一组不同高度的台阶,由一个整数数组表示,数组中每个数是台阶的高度.
当开始下雨了(水足够多),台阶之间的水坑会积多少水呢?

如下图:
可以表示为数组 [0,1,0,2,1,0,1,3,2,1,2,1]
返回积水量 6.


"""

class Solution:
  def trap_waters(self,arr:List[int]):
    N = len(arr)
    if N <=2:
      return 0
    l = 0
    r = N - 1
    prev_h = 0
    total_waters = 0

    def step_area(height:int):
      area = 0
      for steph in arr[l+1: r]:
          h = min(steph,height) - prev_h
          if h > 0:
            area += h
      return area

    while (r - l) > 1:
      lh = arr[l]
      rh = arr[r]
      if lh > prev_h and rh > prev_h:
        width = r - l -1
        if width > 0:
          height = min(rh,lh)
          volume = width * (height - prev_h)
          taked = step_area(height)
          waters = volume - taked
          if waters > 0:
            total_waters += waters
          prev_h = height
      if lh <= prev_h:
        l += 1
      if rh <= prev_h:
        r -= 1
    return total_waters





def test():
  s = Solution()

  assert s.trap_waters([6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]) == 83

  assert s.trap_waters([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
  assert s.trap_waters([0,1,0,2]) == 1
  assert s.trap_waters([0,1]) == 0
  assert s.trap_waters([0,1,2]) == 0
  assert s.trap_waters([0,1,2,1]) == 0
  assert s.trap_waters([0,2,0,1]) == 1
  assert s.trap_waters([0,1,0,2,1,0,1]) == 2
  assert s.trap_waters([0,1,0,2,0,0,1]) == 3
