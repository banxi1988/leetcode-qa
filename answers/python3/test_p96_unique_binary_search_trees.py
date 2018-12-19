# coding: utf-8

__author__ = '代码会说话'

"""
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:

输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

1,2 3, 4,5
"""

import functools
class Solution:
    # @functools.lru_cache(maxsize=None)
    def numTrees(self, n:int) -> int:
        if n == 0:
            return  1
        if n < 3:
            return n
        # print("f(%d)"% n)
        counts = [0] * (n + 1)
        counts[0] = 1
        counts[1] = 1
        counts[2] = 2
        for num in range(2,n + 1):
          count = 0
          for i in range(0, num):
              l = i
              r = num -i -1
              lcount = counts[l]
              rcount = counts[r]
              count += lcount * rcount
          counts[num] = count
        return counts[-1]



def test():
    s = Solution()
    assert s.numTrees(6) == 132
    # return
    assert s.numTrees(3) == 5
    assert s.numTrees(4) == 14
    assert s.numTrees(5) == 42
    assert s.numTrees(19) == 1767263190

