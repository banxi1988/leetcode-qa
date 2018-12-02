# coding: utf-8

__author__ = 'banxi'


class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        count = len(S)
        nums = [0] * (count + 1)

        max_num = count
        min_num = 0
        pos = 0
        for ch in S:
            if ch == 'I':
                nums[pos] = min_num
                min_num+=1
            else:
                nums[pos] = max_num
                max_num-=1
            pos+=1
        nums[pos] = min_num
        return  nums

def test():
    s = Solution()
    assert s.diStringMatch("IDID") == [0,4,1,3,2]
    assert s.diStringMatch("III") == [0,1,2,3]
    assert s.diStringMatch("DDD") == [3,2,1,0]
