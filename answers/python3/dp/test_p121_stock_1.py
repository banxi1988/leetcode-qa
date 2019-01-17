# coding: utf-8

__author__ = '代码会说话'

"""
LeetCode 121. 买卖股票的最佳时机题解 by 代码会说话

给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。

示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。


[7,1,5,3,6,4]

[7,2,10,1,6,8]

buy = 1
[0,0,8,0,5,7]

"""

from typing import List
class Solution:
  def maxProfit(self, prices:List[int]) -> int:
    price_count = len(prices)
    if price_count < 2:
      return 0

    profits = [0] * price_count
    buy = prices[0]
    for i in range(1, price_count):
      price = prices[i]
      if price > buy:
        profits[i] = price - buy
      else:
        buy = price
    return max(profits)





def test():
  s = Solution()
  assert s.maxProfit([7,1,5,3,6,4]) == 5
  assert s.maxProfit([7,6,4,3,2,1]) == 0
  assert s.maxProfit([7,2,10,1,6,8]) == 8
  assert s.maxProfit([7,2,10,1,6,10]) == 9
