# coding: utf-8
class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        return None


def test_wc111_p2():
    s = Solution()
    assert s.minDeletionSize(["a", "b"]) == 0
    assert s.minDeletionSize(["cba", "daf", "ghi"]) == 1
    assert s.minDeletionSize(["zyx", "wvu", "tsr"]) == 3

