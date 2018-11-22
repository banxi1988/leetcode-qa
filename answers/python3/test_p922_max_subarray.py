# coding : utf-8


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if all(num < 0 for num in nums):
            return max(nums)
        count = len(nums)
        maxsums = [0] * count
        if nums[0] > 0:
            maxsums[0] = nums[0]
        for i in range(1, count):
            sum = maxsums[i - 1] + nums[i]
            if sum > 0:
                maxsums[i] = sum
            else:
                maxsums[i] = 0

        return max(maxsums)


def test():
    s = Solution()
    assert s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert s.maxSubArray([-2, 1]) == 1
    assert s.maxSubArray([-2, -2]) == -2
