# coding: utf-8

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

class Solution:
    def subarraysWithKDistinct(self, A: 'List[int]', K: 'int') -> 'int':
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
    # k = 1
    assert s.subarraysWithKDistinct(A = [1,2,3], K = 1) == 3
    assert s.subarraysWithKDistinct(A = [1,2,3,4], K = 1) == 4
    # K =2,core sub =2
    assert s.subarraysWithKDistinct(A=[1, 2, 1], K=2) == 3
    assert s.subarraysWithKDistinct(A=[1,1, 2, 1], K=2) == 5
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
    assert s.subarraysWithKDistinct(A=[1, 2, 1, 2, 3], K=2) == 7
    assert s.subarraysWithKDistinct(A=[1, 2, 1, 3, 4], K=3) == 3

    assert s.subarraysWithKDistinct(A=[1, 2, 1, 2, 3,1], K=3) == 7

    # k =3 core sub =1
    assert s.subarraysWithKDistinct(A = [1,1,2,3], K =3) == 2
    assert s.subarraysWithKDistinct(A = [1,1,2,3,3], K =3) == 4
    # k =3 core sub =2
    assert s.subarraysWithKDistinct(A = [1,1,2,3,1], K =3) == 5
    assert s.subarraysWithKDistinct(A = [1,1,2,3,2,1], K =3) == 8
