# coding: utf-8

__author__ = '代码会说话'

"""
LeetCode 123. 买卖股票的最佳时机 III by 代码会说话

给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [3,3,5,0,0,3,1,4]
输出: 6
解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
示例 2:

输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。   
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。   
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
示例 3:

输入: [7,6,4,3,1] 
输出: 0 
解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。
"""


from typing import List

class Solution:


  def maxProfit(self, prices:List[int]) -> int:
    if not prices:
      return 0

    int_min =  -100 # sys.maxsize
    v1 = int_min # 买了第一次股票之后现金流。
    v2 = int_min # 卖1
    v3 = int_min # 买2
    v4 = int_min # 卖2

    # 第一天股票价格 7
    v1 = -7
    # 第二天股票价格 1
    v1 = max(-7,-1) # -1
    v2 = v1 + 1 # 0
    # 第三天股票价格 5
    v1 = max(-1,-5) # -1
    v2 = max(0,v1 + 5) # 4
    v3 = v2 - 5,-6 #









def test():
  s = Solution()

  assert s.maxProfit([1,2,3,4,5]) == 4
  # return
  assert s.maxProfit([1,2,4,2,5,7,2,4,9,0]) == 13
  assert s.maxProfit([5,4,3,2,1,0,0]) == 0
  assert s.maxProfit([7,1,5,6,5,5,6,2,7]) == 10
  assert s.maxProfit([7,1,5,6,5,4,6,2,7]) == 10
  assert s.maxProfit([7,1,5,3,6,4]) == 7
  assert s.maxProfit([7,6,4,3,1]) == 0
  assert s.maxProfit([1,2,3,4,5]) == 4
  assert s.maxProfit([3,3,5,0,0,3,1,4]) == 6
  assert s.maxProfit(make_large_prices()) == 0

# 199 / 200 个通过测试用例

def make_large_prices():
  l1 = list(range(10000,0,-1))
  l2 = [0] * 16003
  return l1 + l2