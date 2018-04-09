Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).


首先想出一个不完善的解法：

```go
func maxProfit(prices []int) int {
	daysCount := len(prices)
    profit := 0

	for buyIndex := 0; buyIndex < (daysCount - 1); buyIndex++ {
		buyPrice := prices[buyIndex]
		for sellIndex := buyIndex + 1; sellIndex < (daysCount); sellIndex++ {
			sellPrice := prices[sellIndex]
			if sellPrice > buyPrice {
				profit += (sellPrice - buyPrice)
				buyIndex = sellIndex
				break
			}
		}
	}
	return profit
}

```
也就是尽可能多的买卖，但是对于像下面的数据来说：

`maxProfit([]int{7, 1, 2, 5, 6, 4}` 最大收益是 `2`  即 `(2 - 1) + (6 - 5)` 但是其实最大收益 应该是 `6-1`。 也就是 6 和 1 的差值大于其中 2和1 及 6跟5差值的和。
这里需要一个比较。
1）计算出下一个最大的可卖点的最大收益。
2）计算下一个最大可卖点中间的最大收益。
然后取两个收益中的最大值。
在第二步计算时，给人感觉是进入了递归了，但是这个递归会陷入无穷的递归，因为无法收敛。

这里没有考虑到一个情况下，买了之后是否可以马上买。
如果可以的话。 `6-1` 也相当于 `(2-1) + (5-2) + (6-5)`,也就是说，中间没有比 `6-1` 大的情况意味着。他们累积的差跟`6-1` 直接的差是一样的。于是计算的时候直接就转成了累加的逻辑了。
考虑其中可能的另一种情况，就是如果 `1` 到 `6` 不是递增的，那我们的逻辑会有什么问题？即将上面数据修改成,
`7,1,3,2,5,6,4` ,此时最大收益是 `(3-1) + (6-2)`,这样可以看出来，其实最大收益就是所有递增区间的累加的和。
得到如下代码解答：

```go
func maxProfit(prices []int) int {
	max := 0
	daysCount := len(prices)
	for sellIndex := 1; sellIndex < daysCount; sellIndex++ {
		profit := prices[sellIndex] - prices[sellIndex-1]
		if profit > 0 {
			max += profit
		}
	}
	return max
}
```
