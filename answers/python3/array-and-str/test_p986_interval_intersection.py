# coding: utf-8

__author__ = '代码会说话'

"""
给定两个由一些闭区间组成的列表，每个区间列表都是成对不相交的，并且已经排序。

返回这两个区间列表的交集。

（形式上，闭区间 [a, b]（其中 a <= b）表示实数 x 的集合，而 a <= x <= b。两个闭区间的交集是一组实数，要么为空集，要么为闭区间。例如，[1, 3] 和 [2, 4] 的交集为 [2, 3]。）

 

示例：



输入：A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
输出：[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
注意：输入和所需的输出都是区间对象组成的列表，而不是数组或列表。
 

提示：

0 <= A.length < 1000
0 <= B.length < 1000
0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9
"""


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def __eq__(self, other):
      return other.start == self.start and other.end == self.end

    def __str__(self):
      return "%d-%d" % (self.start,self.end)

    def __repr__(self):
      return str(self)

from typing import List
class Solution:
  def intervalIntersection(self, A: 'List[Interval]', B: 'List[Interval]') -> 'List[Interval]':
    a_len = len(A)
    b_len = len(B)
    ai = 0
    bi = 0
    results = []
    while ai < a_len and bi < b_len:
      ra = A[ai]
      rb = B[bi]
      s = max(ra.start,rb.start)
      e = min(ra.end, rb.end)
      if e >= s:
        results.append(Interval(s,e))

      if ra.end == rb.end:
        ai += 1
        bi += 1
      elif ra.end < rb.end:
        ai += 1
      else:
        bi += 1
    return results

def ll2il(ll:List[List[int]]):
  return [Interval(r[0],r[1]) for r in ll]

def test():
  s = Solution()
  r1 = s.intervalIntersection(A = ll2il([[0,2],[5,10],[13,23],[24,25]]), B = ll2il([[1,5],[8,12],[15,24],[25,26]]))
  assert r1 == ll2il([[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]])