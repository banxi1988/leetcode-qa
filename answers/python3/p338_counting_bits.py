# coding: utf-8

__author__ = '代码会说话'

"""
LeetCode 338. 比特位计数 题解 by @代码会说话

给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。

示例 1:

输入: 2
输出: [0,1,1]
示例 2:

输入: 5
输出: [0,1,1,2,1,2]
进阶:

给出时间复杂度为O(n*sizeof(integer))的解答非常容易。但你可以在线性时间O(n)内用一趟扫描做到吗？
要求算法的空间复杂度为O(n)。
你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数（如 C++ 中的 __builtin_popcount）来执行此操作。

0 -> 0000  -> 0
1 -> 0001  -> 1
2 -> 0010  -> 1 
3 -> 0011  -> 2  bits[3] = bits[2] + 1 = 2
4 -> 0100  -> 1
5 -> 0101  -> 2  bits[4] + 1 = 2
6 -> 0110  -> 2  bits[4] + bits[2] = 2
7 -> 0111  -> 3  bits[4] + bits[3] = 3
8 -> 1000  -> 1  bits[8] = 1
9 -> 1001  -> 2  bits[8] + bits[1] = 2
10 -> 1010  -> 2 bits[8] + bits[2] = 2
11 -> 1011  -> 3
12 -> 1100  -> 2
13 -> 1101  -> 3
14 -> 1110  -> 3
15 -> 1111  -> 4 bits[8] + bits[7] = 1 + 3 = 4
16 -> 10000  -> 1
17 -> 10001  -> 2

"""

from typing import List

class Solution:
    def countBits(self, num:int) -> List[int]:
        if num == 0:
            return  [0]
        if num == 1:
            return  [0,1]
        base = 2
        bits = [0] * (num + 1) #  int [num+1];
        bits[1] = 1
        bits[2] = 1
        cur_num = 3
        while cur_num <= num:
            next_base = base * 2
            cur_num = base + 1
            while cur_num <= num and cur_num < next_base:
                bits[cur_num] = 1 + bits[cur_num - base]
                cur_num+=1
            if next_base <= num:
                bits[next_base] = 1
            base = next_base
        return bits



def test():
    s = Solution()
    assert s.countBits(0) == [0]
    assert s.countBits(1) == [0,1]
    assert s.countBits(2) == [0,1,1]
    assert s.countBits(5) == [0,1,1,2,1,2]
    assert s.countBits(6) == [0,1,1,2,1,2,2]
    assert s.countBits(7) == [0,1,1,2,1,2,2,3]
    assert s.countBits(8) == [0,1,1,2,1,2,2,3,1]
    assert s.countBits(9) == [0,1,1,2,1,2,2,3,1,2]
    assert s.countBits(10) == [0,1,1,2,1,2,2,3,1,2,2]
    assert s.countBits(11) == [0,1,1,2,1,2,2,3,1,2,2,3]
    assert s.countBits(12) == [0,1,1,2,1,2,2,3,1,2,2,3,2]
    assert s.countBits(13) == [0,1,1,2,1,2,2,3,1,2,2,3,2,3]
    assert s.countBits(14) == [0,1,1,2,1,2,2,3,1,2,2,3,2,3,3]
    assert s.countBits(15) == [0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4]
    assert s.countBits(16) == [0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4,1]
    assert s.countBits(17) == [0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4,1,2]

