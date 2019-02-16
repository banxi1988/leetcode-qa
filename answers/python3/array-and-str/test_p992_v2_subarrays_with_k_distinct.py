# coding: utf-8
from typing import List

__author__ = '代码会说话'

"""
给定一个正整数数组 A，如果 A 的某个子数组中不同整数的个数恰好为 K，则称 A 的这个连续、不一定独立的子数组为好子数组。

（例如，[1,2,3,1,2] 中有 3 个不同的整数：1，2，以及 3。）

返回 A 中好子数组的数目。

 

示例 1：

输出：A = [1,2,1,2,3], K = 2
输入：7
解释：恰好由 2 个不同整数组成的子数组：[1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
示例 2：

输入：A = [1,2,1,3,4], K = 3
输出：3
解释：恰好由 3 个不同整数组成的子数组：[1,2,1,3], [2,1,3], [1,3,4].
 

提示：

1 <= A.length <= 20000
1 <= A[i] <= A.length
1 <= K <= A.length

K = 1
1,2,3

"""

import collections

class SlidingWindow:
    def __init__(self):
        self.counter = collections.Counter()
        self.num_count = 0

    def add(self,num:int):
        self.counter[num] += 1
        if self.counter[num] == 1:
            self.num_count += 1

    def remove(self,num:int):
        self.counter[num] -= 1
        if self.counter[num] == 0:
            self.num_count -= 1



class KRange:
    def __init__(self,A:List[int],K:int):
        self.A = A
        self.K = K
        self.alen = len(A)
        self.num_counter = collections.Counter()
        self.distinct_count = 0
        self.i = 0
        self.j = 0

    def expand(self):
        num = self.A[self.j]
        self.j += 1
        self.num_counter[num] += 1
        if self.num_counter[num] == 1:
            self.distinct_count += 1

    def forward(self):
        num = self.A[self.i]
        self.i += 1
        self.num_counter[num] -= 1
        if self.num_counter[num] == 0:
            self.distinct_count -= 1

    def expand_to_max(self):
        while self.can_expand():
            self.expand()
        return self.distinct_count == self.K

    def can_expand(self):
        if self.j < self.alen:
          if self.distinct_count < self.K:
              return True
          num = self.A[self.j]
          return self.num_counter[num] > 0
        else:
            return False

    def can_move_forward(self):
        return self.j < self.alen

    def expand_to_K(self):
        while self.distinct_count < self.K and self.j < self.alen:
            self.expand()
        self.trim_left()
        return self.distinct_count == self.K

    def trim_left(self):
        if self.distinct_count == self.K:
            while (self.i + 1) < self.j :
                i = self.i
                num = self.A[self.i]
                if num == self.A[i+1]:
                  self.i += 1
                  self.num_counter[num] -= 1
                else:
                  break

    def range_slice(self):
        return self.A[self.i:self.j]

class Solution:
    def subarraysWithKDistinct(self, A: 'List[int]', K: 'int') -> 'int':
        maxkrange = KRange(A=A,K=K)
        total_count = 0
        while maxkrange.can_move_forward():
            if not maxkrange.expand_to_max():
                break
            n = maxkrange.j - maxkrange.i
            prev_i = -1
            minkrange = KRange(A=maxkrange.range_slice(),K=K)
            while minkrange.expand_to_K():
              count = (minkrange.i - (prev_i + 1) + 1) * (n - minkrange.j + 1)
              total_count += count
              prev_i = minkrange.i
              minkrange.forward()
            while maxkrange.distinct_count >= K:
                maxkrange.forward()

        return total_count



        sw1 = SlidingWindow()
        sw2 = SlidingWindow()
        result = 0
        left1 = 0
        left2 = 0
        for right,num in enumerate(A):
            sw1.add(num)
            sw2.add(num)
            while sw1.num_count > K:
                sw1.remove(A[left1])
                left1 += 1

            while sw2.num_count >= K:
                sw2.remove(A[left2])
                left2 += 1

            result += left2 - left1
        return result



def test():
    s = Solution()
    assert s.subarraysWithKDistinct(A = [5,7,5,2,3,3,4,1,5,2,7,4,6,6,3,3,4,4,7], K=7) == 52
    assert s.subarraysWithKDistinct(A = [2,1,1,1,2],K =1) == 8
    assert s.subarraysWithKDistinct(A = [2,1,2,1,1], K=3) == 0
    assert s.subarraysWithKDistinct(A=[1, 2, 1, 2, 3], K=2) == 7

    # k = 1
    assert s.subarraysWithKDistinct(A = [1,2,3], K = 1) == 3
    assert s.subarraysWithKDistinct(A = [1,2,3,4], K = 1) == 4
    # K =2,core sub =2
    assert s.subarraysWithKDistinct(A=[1,1, 2, 1], K=2) == 5
    assert s.subarraysWithKDistinct(A=[1, 2, 1], K=2) == 3
    assert s.subarraysWithKDistinct(A=[1,1, 2, 1,1], K=2) == 8
    assert s.subarraysWithKDistinct(A=[1,1, 2,2, 1,1], K=2) == 12

    # k =2 core sub =3
    assert s.subarraysWithKDistinct(A=[1, 2, 1,2], K=2) == 6
    assert s.subarraysWithKDistinct(A=[1,1, 2, 1,2,2], K=2) == 13
    assert s.subarraysWithKDistinct(A=[1,1, 2,2, 1,2,2], K=2) == 18

    assert s.subarraysWithKDistinct(A=[1, 1, 2, 2], K=2) == 4
    assert s.subarraysWithKDistinct(A=[1, 1, 1, 2, 2,2], K=2) == 9
    assert s.subarraysWithKDistinct(A=[1, 1, 1, 1, 2,2,2], K=2) == 12
    assert s.subarraysWithKDistinct(A=[1, 1, 1, 1, 1,2], K=2) == 5
    assert s.subarraysWithKDistinct(A=[1, 1, 1, 1, 1,2,2], K=2) == 10
    assert s.subarraysWithKDistinct(A=[1, 1, 1, 1, 2,2,2,2], K=2) == 16
    assert s.subarraysWithKDistinct(A=[1, 1, 1, 1, 1,2,2,2], K=2) == 15
    assert s.subarraysWithKDistinct(A=[1, 2, 1, 2, 3], K=1) == 5
    assert s.subarraysWithKDistinct(A=[1, 2, 1, 2, 3], K=3) == 3
    assert s.subarraysWithKDistinct(A=[1, 2, 1, 3, 4], K=3) == 3

    assert s.subarraysWithKDistinct(A=[1, 2, 1, 2, 3,1], K=3) == 7

    # k =3 core sub =1
    assert s.subarraysWithKDistinct(A = [1,1,2,3], K =3) == 2
    assert s.subarraysWithKDistinct(A = [1,1,2,3,3], K =3) == 4
    # k =3 core sub =2
    assert s.subarraysWithKDistinct(A = [1,1,2,3,1], K =3) == 5
    assert s.subarraysWithKDistinct(A = [1,1,2,3,2,1], K =3) == 8
