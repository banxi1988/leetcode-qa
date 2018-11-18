# coding: utf-8
class Solution:
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        count = len(A)
        if count < 3:
            return False
        i = 1
        has_left_valley = False
        has_right_valley = False
        check_inc = True
        while i < count:
            prev = A[i - 1]
            cur = A[i]
            if check_inc:
                if cur > prev:
                    has_left_valley = True
                elif cur == prev:
                    return False
                else:
                    has_right_valley = True
                    check_inc = False
            else:
                if cur < prev:
                    has_right_valley = True
                else:
                    return False

            i += 1

        return has_left_valley and has_right_valley


def test_wc111_p1():
    s = Solution()
    assert s.validMountainArray([2, 1]) == False
    assert s.validMountainArray([3, 5, 5]) == False
    assert s.validMountainArray([1, 2, 1]) == True
    assert s.validMountainArray([0, 3, 2, 1]) == True
    assert s.validMountainArray([0, 3, 2, 1, 2]) == False
    assert s.validMountainArray([1, 2, 3, 4]) == False
    assert s.validMountainArray([4, 3, 1, 1]) == False

