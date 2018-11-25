#coding: utf-8

"""
945. 使数组唯一的最小增量
题目难度 Medium
给定整数数组 A，每次 move 操作将会选择任意 A[i]，并将其递增 1。

返回使 A 中的每个值都是唯一的最少操作次数。
"""
from collections import defaultdict


class Solution:
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        nums = sorted(A)
        room_to_count = {}
        duplicate_nums = []
        for num in nums:
            if num in room_to_count:
                duplicate_nums.append(num)
            else:
                room_to_count[num] = num
        if len(duplicate_nums) < 1:
            return  0
        room_no = duplicate_nums[0] + 1
        moves = 0
        for num in duplicate_nums:
            room_no = max(num +1, room_no)
            while True:
                if room_no not in room_to_count:
                    room_to_count[room_no] = num
                    moves += room_no - num
                    room_no+=1
                    break
                room_no+=1
        return  moves



def test():
    s = Solution()
    assert s.minIncrementForUnique([1,2,2]) == 1
    assert s.minIncrementForUnique([3,2,1,2,1,7]) == 6
    assert s.minIncrementForUnique([14,4,5,14,13,14,10,17,2,12,2,14,7,13,14,13,4,16,4,10]) == 41
