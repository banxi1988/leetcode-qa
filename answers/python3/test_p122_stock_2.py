# coding: utf-8

__author__ = '代码会说话'

"""
LeetCode 122. 买卖股票的最佳时机 II by 代码会说话

给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
示例 2:

输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
示例 3:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。



[7,1,5,3,6,4]

[7,1,5,6,5,5,6,2,7]

6-1,6-5,7-2
peek = 7
valley = 2



"""

from typing import List

class Solution:
  def maxProfit(self, prices:List[int]) -> int:
    if not prices:
      return 0
    peek = 0
    valley = prices[0]
    profits = []
    for price in prices[1:]:
      if price < peek:
        profits.append(peek - valley)
        valley=price
        peek=0
      else:
        if price > peek:
          peek = price
        if price < valley:
          valley = price
    if peek > valley:
      profits.append(peek - valley)
    return sum(profits)




def test():
  s = Solution()
  assert s.maxProfit([7,1,5,6,5,5,6,2,7]) == 11
  assert s.maxProfit([7,1,5,6,5,4,6,2,7]) == 12
  assert s.maxProfit([7,1,5,3,6,4]) == 7
  assert s.maxProfit([7,6,4,3,1]) == 0
  assert s.maxProfit([1,2,3,4,5]) == 4
