# coding : utf-8


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        count = len(prices)
        if count < 2:
            return 0
        maxbuys = [0] * count
        max_after_i = [0] * count  # max_after_i[2] 表示 prices[2]  到 prices[n-1] 之间的最大值
        maxi = prices[count - 1]
        max_after_i[count - 1] = maxi
        for i in range(count - 2, -1, -1):
            if prices[i] > maxi:
                maxi = prices[i]
            max_after_i[i] = maxi

        for i in range(0, count - 1):
            pi = prices[i]
            maxnext = max_after_i[i + 1]
            if maxnext > pi:
                maxbuys[i] = maxnext - pi

        return max(maxbuys)


def test():
    s = Solution()

    assert s.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert s.maxProfit([7, 6, 4, 3, 1]) == 0
    assert s.maxProfit([7, 1, 5, 3, 6, 4, 7]) == 6
    assert s.maxProfit([7, 8]) == 1
    assert s.maxProfit([7, 8, 9]) == 2
    assert s.maxProfit([7, 6, 9]) == 3
    assert s.maxProfit([]) == 0
    assert s.maxProfit([3]) == 0

