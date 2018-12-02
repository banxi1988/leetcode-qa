#coding: utf-8

"""
给定一个由 4 位数字组成的数组，返回可以设置的符合 24 小时制的最大时间。

最小的 24 小时制时间是 00:00，而最大的是 23:59。从 00:00 （午夜）开始算起，过得越久，时间越大。

以长度为 5 的字符串返回答案。如果不能确定有效时间，则返回空字符串。



示例 1：

输入：[1,2,3,4]
输出："23:41"
示例 2：

输入：[5,5,5,5]
输出：""

A.length == 4
0 <= A[i] <= 9

"""
from collections import defaultdict


class Solution:
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        num_count = defaultdict(int)
        for num in A:
            num_count[num] += 1
        for hour in range(23,-1,-1):
            hs = str(hour) if hour > 9 else '0'+str(hour)
            d1 = int(hs[0])
            d2 = int(hs[1])
            if not ((d1 == d2 and num_count[d1] > 1) or ((d1 != d2) and num_count[d1] and num_count[d2])):
                continue
            num_count[d1] -=1
            num_count[d2] -=1
            for minute in range(59,-1,-1):
                ms = str(minute) if minute > 9 else '0' +str(minute)
                d3 = int(ms[0])
                d4 = int(ms[1])
                if (d3 == d4 and num_count[d3] > 1) or(d3 != d4 and  num_count[d3] and num_count[d4]):
                    return hs+":"+ms

            num_count[d1] +=1
            num_count[d2] +=1
        return ""






def test():
    s = Solution()
    assert s.largestTimeFromDigits([2,0,6,6]) == "06:26"
    assert s.largestTimeFromDigits([0,0,0,0]) == "00:00"
    assert s.largestTimeFromDigits([1,2,3,4]) == "23:41"
    assert s.largestTimeFromDigits([5,5,5,5]) == ""
