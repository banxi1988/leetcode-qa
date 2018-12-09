# coding: utf-8

__author__ = 'banxi'

"""
LeetCode 954. 二倍数对数组

给定一个长度为偶数的整数数组 A，只有对 A 进行重组后可以满足 “对于每个 0 <= i < len(A) / 2，都有 A[2 * i + 1] = 2 * A[2 * i]” 时，返回 true；否则，返回 false。

A[1] = 2 * A[0]
A[3] = 2 * A[2] 
A[5] = 2 * A[3] 
 

示例 1：

输入：[3,1,3,6]
输出：false
示例 2：

输入：[2,1,2,6]
输出：false
示例 3：

输入：[4,-2,2,-4]
输出：true
解释：我们可以用 [-2,-4] 和 [2,4] 这两组组成 [-2,-4,2,4] 或是 [2,4,-2,-4]
示例 4：

输入：[1,2,4,16,8,4]
输出：false
 

提示：

0 <= A.length <= 30000
A.length 为偶数
-100000 <= A[i] <= 100000
"""
from typing import  List
from collections import Counter

class Solution:
    def canReorderDoubled(self, A:List[int]) -> bool:

        num_to_count = Counter(A)
        result_arr = []
        for num in sorted(A):
            double_num = num * 2
            num_count = num_to_count.get(num, 0)
            d_count = num_to_count.get(double_num, 0)
            if num_count > 0 and d_count > 0:
                result_arr.append((num,double_num))
                num_to_count[num] -=1
                num_to_count[double_num] -=1

        return len(result_arr) == len(A) /2


def test():
    s = Solution()
    assert s.canReorderDoubled([1,2,1,-8,8,-4,4,-4,2,-2]) == True
    assert s.canReorderDoubled([3,1,3,6]) == False
    assert s.canReorderDoubled([2,1,2,6]) == False
    assert s.canReorderDoubled([4,-2,2,-4]) == True
    assert s.canReorderDoubled([1,2,4,16,8,4]) == False
